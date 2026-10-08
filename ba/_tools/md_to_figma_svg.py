"""Render a condensed outline (figma.md) into an SVG canvas that can be dragged into Figma.

Usage: python md_to_figma_svg.py <figma.md> [--theme dark|light] [--out file.svg]

Outline syntax:
  === [width]        start a new row (first column of the row, optional width px)
  --- [width]        start a new column in the current row
  # Title            big title
  ## HEADING         section heading (yellow on dark theme)
  - item / 1. item   bullets, 2 spaces of indent per level
  plain text         paragraph (indent = level)
  ```                fenced block (SQL...), rendered monospace, no inline parsing
  ![caption|900](path.png)   embedded PNG, optional width after |
  **bold**  ==orange (change)==  !!red (warning)!!  `mono`
  <!-- comment -->   ignored
"""
import argparse
import base64
import re
import struct
import sys
import unicodedata
from pathlib import Path

THEMES = {
    "dark": dict(bg="#2C2C2C", text="#E6E6E6", heading="#F5C518", title="#FFFFFF",
                 orange="#F2994A", red="#FF6B6B", code="#9CDCFE", caption="#A0A0A0", border="#555555"),
    "light": dict(bg="#F0F0F0", text="#1E1E1E", heading="#111111", title="#111111",
                  orange="#D9730D", red="#D92D20", code="#1F5FAD", caption="#6B6B6B", border="#C8C8C8"),
}

FONT = "Inter"
MONO = "Roboto Mono"
SIZE = 16
LINE = 24
H_SIZE, H_LINE = 19, 30
T_SIZE, T_LINE = 30, 42
CODE_SIZE, CODE_LINE = 14, 21
CAP_SIZE, CAP_LINE = 13, 19
INDENT = 22
COL_W = 900
COL_GAP = 100
ROW_GAP = 90
PAD = 60

# Approximate Inter advance widths (em). Unknown chars fall back to 0.6.
_W = {
    " ": .27, "a": .55, "b": .6, "c": .53, "d": .6, "e": .56, "f": .35, "g": .6, "h": .58, "i": .23,
    "j": .23, "k": .52, "l": .23, "m": .87, "n": .58, "o": .58, "p": .6, "q": .6, "r": .36, "s": .51,
    "t": .35, "u": .58, "v": .53, "w": .78, "x": .52, "y": .53, "z": .51,
    "A": .68, "B": .64, "C": .7, "D": .71, "E": .6, "F": .58, "G": .72, "H": .72, "I": .27, "J": .5,
    "K": .66, "L": .55, "M": .84, "N": .72, "O": .74, "P": .63, "Q": .74, "R": .64, "S": .63, "T": .62,
    "U": .7, "V": .68, "W": .97, "X": .66, "Y": .66, "Z": .62,
    ".": .26, ",": .26, ":": .26, ";": .26, "'": .2, '"': .35, "(": .33, ")": .33, "[": .33, "]": .33,
    "-": .4, "–": .6, "—": 1.0, "/": .38, "_": .5, "=": .6, "<": .6, ">": .6, "*": .45,
    "→": .85, "•": .5, "·": .3, "!": .28, "?": .5, "%": .85, "&": .7, "@": 1.0, "#": .65,
    "+": .6, "|": .3, "~": .6, "…": .9, "“": .35, "”": .35, "≥": .6, "≤": .6,
}
for _d in "0123456789":
    _W[_d] = .6


def char_w(ch, size, bold=False, mono=False):
    if mono:
        return .6 * size
    if unicodedata.combining(ch):
        return 0
    base = {"đ": "d", "Đ": "D"}.get(ch) or unicodedata.normalize("NFD", ch)[0]
    w = _W.get(base, .6) * size * 1.04
    return w * 1.05 if bold else w


def text_w(s, size, bold=False, mono=False):
    return sum(char_w(c, size, bold, mono) for c in s)


INLINE = re.compile(r"\*\*(.+?)\*\*|==(.+?)==|!!(.+?)!!|`(.+?)`")


def parse_inline(s, style):
    out, pos = [], 0
    for m in INLINE.finditer(s):
        if m.start() > pos:
            out.append((s[pos:m.start()], style))
        if m.group(1) is not None:
            out += parse_inline(m.group(1), {**style, "bold": True})
        elif m.group(2) is not None:
            out += parse_inline(m.group(2), {**style, "color": "orange"})
        elif m.group(3) is not None:
            out += parse_inline(m.group(3), {**style, "color": "red", "bold": True})
        else:
            out.append((m.group(4), {**style, "mono": True, "color": "code"}))
        pos = m.end()
    if pos < len(s):
        out.append((s[pos:], style))
    return out


def wrap(runs, width, size):
    """Greedy word wrap over styled runs -> list of lines, each a list of (text, style)."""
    tokens = []
    for text, st in runs:
        for tok in re.findall(r"\S+\s*|\s+", text):
            tokens.append((tok, st))
    lines, cur, cur_w = [], [], 0.0
    for tok, st in tokens:
        w = text_w(tok, size, st.get("bold"), st.get("mono"))
        if cur and cur_w + text_w(tok.rstrip(), size, st.get("bold"), st.get("mono")) > width:
            lines.append(cur)
            cur, cur_w = [], 0.0
            tok = tok.lstrip()
            if not tok:
                continue
            w = text_w(tok, size, st.get("bold"), st.get("mono"))
        while w > width and not cur:
            # Hard-break a token longer than the line.
            n, acc = 0, 0.0
            while n < len(tok) and acc + char_w(tok[n], size, st.get("bold"), st.get("mono")) <= width:
                acc += char_w(tok[n], size, st.get("bold"), st.get("mono"))
                n += 1
            n = max(n, 1)
            lines.append([(tok[:n], st)])
            tok = tok[n:]
            w = text_w(tok, size, st.get("bold"), st.get("mono"))
        if tok:
            cur.append((tok, st))
            cur_w += w
    if cur:
        lines.append(cur)
    return lines or [[("", {})]]


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def png_size(data):
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("only PNG images are supported")
    return struct.unpack(">II", data[16:24])


# ---------------------------------------------------------------- parsing

def parse(md_text):
    rows = [[{"w": COL_W, "items": []}]]

    def new_col(width, new_row):
        col = rows[-1][-1]
        if not col["items"]:
            if new_row and len(rows[-1]) > 1:
                rows[-1].pop()
                rows.append([col])
            col["w"] = width or col["w"]
            return
        col = {"w": width or COL_W, "items": []}
        if new_row:
            rows.append([col])
        else:
            rows[-1].append(col)

    lines = md_text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip()
        items = rows[-1][-1]["items"]
        m = re.match(r"^(===|---)\s*(\d+)?\s*$", raw)
        if m:
            new_col(int(m.group(2)) if m.group(2) else None, m.group(1) == "===")
            i += 1
            continue
        if raw.strip().startswith("<!--"):
            while "-->" not in lines[i]:
                i += 1
            i += 1
            continue
        if not raw.strip():
            if items and items[-1][0] != "gap":
                items.append(("gap",))
            i += 1
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        s = raw.strip()
        if s.startswith("```"):
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i].rstrip()[indent:] if lines[i][:indent].strip() == "" else lines[i].rstrip())
                i += 1
            items.append(("code", code, indent // 2))
            i += 1
            continue
        if s.startswith("# "):
            items.append(("title", s[2:]))
        elif s.startswith("## "):
            items.append(("h", s[3:]))
        elif (mi := re.match(r"^!\[(.*?)\]\((.+?)\)$", s)):
            cap, _, w = mi.group(1).partition("|")
            items.append(("img", mi.group(2), cap.strip(), int(w) if w.strip() else None, indent // 2))
        elif (mb := re.match(r"^([-*]|\d+\.)\s+(.*)$", s)):
            marker = "•" if mb.group(1) in "-*" else mb.group(1)
            items.append(("li", mb.group(2), indent // 2 + 1, marker))
        else:
            items.append(("p", s, indent // 2))
        i += 1
    return rows


# ---------------------------------------------------------------- rendering

class Canvas:
    def __init__(self, theme, base_dir):
        self.t = THEMES[theme]
        self.base = base_dir
        self.out = []

    def line(self, x, y, runs, size, default_color="text", base_bold=False, italic=False, family=FONT):
        parts, last = [], None
        for text, st in runs:
            key = (st.get("bold") or base_bold, st.get("color", default_color), st.get("mono", False))
            if parts and key == last:
                parts[-1][1] += text
            else:
                parts.append([key, text])
                last = key
        spans = []
        for (bold, color, mono), text in parts:
            attrs = f' fill="{self.t[color]}"'
            if bold:
                attrs += ' font-weight="700"'
            if mono and family != MONO:
                attrs += f' font-family="{MONO}"'
            spans.append(f"<tspan{attrs}>{esc(text)}</tspan>")
        style = ' font-style="italic"' if italic else ""
        self.out.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="{family}" font-size="{size}"{style}>'
                        + "".join(spans) + "</text>")

    def flow(self, x, y, width, runs, size, lh, **kw):
        for ln in wrap(runs, width, size):
            self.line(x, y + size, ln, size, **kw)
            y += lh
        return y

    def column(self, x, y, col):
        w = col["w"]
        prev = None
        for it in col["items"]:
            kind = it[0]
            if kind == "gap":
                y += 10
            elif kind == "title":
                y = self.flow(x, y, w, parse_inline(it[1], {}), T_SIZE, T_LINE, default_color="title", base_bold=True) + 8
            elif kind == "h":
                if prev not in (None, "gap"):
                    y += 14
                y = self.flow(x, y, w, parse_inline(it[1], {}), H_SIZE, H_LINE, default_color="heading", base_bold=True) + 4
            elif kind == "li":
                _, text, level, marker = it
                tx = x + level * INDENT
                bx = tx - INDENT + (6 if marker == "•" else 0)
                self.out.append(f'<text x="{bx:.0f}" y="{y + SIZE:.0f}" font-family="{FONT}" font-size="{SIZE}" '
                                f'fill="{self.t["text"]}">{esc(marker)}</text>')
                y = self.flow(tx, y, w - (tx - x), parse_inline(text, {}), SIZE, LINE)
            elif kind == "p":
                tx = x + it[2] * INDENT
                y = self.flow(tx, y, w - (tx - x), parse_inline(it[1], {}), SIZE, LINE)
            elif kind == "code":
                tx = x + it[2] * INDENT
                y += 4
                for src in it[1]:
                    lead = len(src) - len(src.lstrip(" "))
                    src = " " * lead + src[lead:]
                    y = self.flow(tx, y, w - (tx - x), [(src, {"mono": True})], CODE_SIZE, CODE_LINE,
                                  default_color="code", family=MONO)
                y += 6
            elif kind == "img":
                _, path, cap, iw, level = it
                tx = x + level * INDENT
                data = (self.base / path).read_bytes()
                pw, ph = png_size(data)
                iw = min(iw or (w - (tx - x)), w - (tx - x))
                ih = ph * iw / pw
                y += 6
                b64 = base64.b64encode(data).decode()
                self.out.append(f'<image x="{tx:.0f}" y="{y:.0f}" width="{iw:.0f}" height="{ih:.0f}" '
                                f'preserveAspectRatio="xMidYMid meet" href="data:image/png;base64,{b64}" '
                                f'xlink:href="data:image/png;base64,{b64}"/>')
                self.out.append(f'<rect x="{tx:.0f}" y="{y:.0f}" width="{iw:.0f}" height="{ih:.0f}" fill="none" '
                                f'stroke="{self.t["border"]}" stroke-width="1"/>')
                y += ih + 8
                if cap:
                    y = self.flow(tx, y, iw, parse_inline(cap, {}), CAP_SIZE, CAP_LINE,
                                  default_color="caption", italic=True)
                y += 8
            prev = kind
        return y

    def render(self, rows):
        y, max_x = PAD, 0
        for row in rows:
            x, row_bottom = PAD, y
            for col in row:
                row_bottom = max(row_bottom, self.column(x, y, col))
                x += col["w"] + COL_GAP
            max_x = max(max_x, x - COL_GAP)
            y = row_bottom + ROW_GAP
        W, H = max_x + PAD, y - ROW_GAP + PAD
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
                f'width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}" xml:space="preserve" '
                f'style="white-space:pre">'
                f'<rect width="{W:.0f}" height="{H:.0f}" fill="{self.t["bg"]}"/>')
        return head + "\n".join(self.out) + "</svg>\n"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("--theme", choices=THEMES, default="dark")
    ap.add_argument("--out")
    a = ap.parse_args()
    src = Path(a.md)
    out = Path(a.out) if a.out else src.with_suffix(".svg")
    rows = parse(src.read_text(encoding="utf-8"))
    out.write_text(Canvas(a.theme, src.parent).render(rows), encoding="utf-8")
    print(f"OK -> {out}")


if __name__ == "__main__":
    main()
