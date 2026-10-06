#!/usr/bin/env python3
"""
Render the "whoami" panel -- a terminal window that types itself out, line by
line -- as bio.svg. It sits beside stats.svg in the README, so the canvas is the
same 840 x 880 and both panels line up at equal display widths.

Everything here is data: edit PROFILE / SKILLS / NOW below and re-run, or point
the script at a JSON file:

    python scripts/render_bio_svg.py [profile.json] [output.svg]

Each output line types on character by character (SMIL <set> over pre-rendered
prefix frames, staggered), then the highlight lines and the skill chips fade in,
and a status-bar cursor blinks forever. GitHub runs SMIL/CSS inside <img> SVGs
but never JS, so no scripting is used.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "bio.json")
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "..", "bio.svg")

PROFILE = {
    "host": "atul@github",
    "name": "Atul Kumar Choudhary",
    "role": "Full-Stack AI Engineer",
    "focus": "data platforms / distributed systems / AI",
    "handle": "github.com/atul-kumar-choudhary",
    "links": [
        ("portfolio", "atulchoudhary.com"),
        ("linkedin", "in/atulkumarchoudhary"),
        ("email", "dev@atulchoudhary.com"),
    ],
    "now": [
        "building decision intelligence platforms",
        "deep-diving advanced analytics + data engineering",
        "writing the best code between 5 - 7 AM",
    ],
    "skills": [
        ("languages", ["Python", "TypeScript", "Go", "Rust", "C++", "SQL"]),
        ("stack", ["Next.js", "React", "Tailwind", "FastAPI", "Node.js", "Docker"]),
        ("infra", ["PostgreSQL", "MongoDB", "Redis", "Kafka", "Kubernetes", "AWS"]),
    ],
}

BG = "#0d1117"
BG2 = "#111722"
TILE = "#161b22"
FRAME = "#30363d"
MUTED = "#7d8590"
INK = "#e6edf3"
GREEN = "#39d353"
CYAN = "#22d3ee"
GOLD = "#f2cc60"
VIOLET = "#a371f7"

W, H = 840, 880                      # == stats.svg canvas
PAD = 20
TITLEBAR_H = 30
STATUS_H = 30
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
FS = 22                             # body text size
CH = FS * 0.6                       # monospace advance width at FS
LINE_H = 38

# timing (seconds)
TYPE_START = 0.35
CHAR_T = 0.018                      # per character
LINE_GAP = 0.16                     # pause between lines
MAX_FRAMES = 28                     # keystrokes per line (keeps the SVG small)


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def typed(text, x, y, t0, color=INK, weight="400", frames=None, per_char=CHAR_T):
    """One <text> per rendered prefix, revealed by chained <set> begin times.

    A static copy of the finished line sits behind the animation and is only
    shown when the visitor prefers reduced motion, so the panel is never blank
    if SMIL is unavailable.
    """
    frames = frames or max(3, min(len(text), MAX_FRAMES))
    out = [f'<g class="type">']
    for k in range(1, frames + 1):
        p = k / frames
        shown = text[: max(1, int(round(len(text) * p)))]
        t_on = t0 + per_char * (k - 1)
        t_off = t0 + per_char * k
        anim = f'<set attributeName="opacity" to="1" begin="{t_on:.3f}s"/>'
        if k < frames:
            anim += f'<set attributeName="opacity" to="0" begin="{t_off:.3f}s"/>'
        out.append(
            f'<text x="{x:.1f}" y="{y:.1f}" opacity="0" fill="{color}" font-size="{FS}" '
            f'font-weight="{weight}" xml:space="preserve">{esc(shown)}{anim}</text>'
        )
    out.append('</g>')
    out.append(
        f'<text class="static" x="{x:.1f}" y="{y:.1f}" fill="{color}" font-size="{FS}" '
        f'font-weight="{weight}" xml:space="preserve">{esc(text)}</text>'
    )
    return "".join(out)


def fade(inner, t0, dur=0.45):
    return f'<g opacity="0" style="opacity:0;animation:fadein {dur}s ease-out {t0:.2f}s both">{inner}</g>'


def type_dur(text):
    """How long typed() takes to finish this string -- keep scheduling in sync."""
    return max(3, min(len(text), MAX_FRAMES)) * CHAR_T


if os.path.exists(SRC):
    PROFILE.update(json.load(open(SRC)))

host = PROFILE["host"]
lines = [
    ("name", PROFILE["name"], INK, "700"),
    ("role", PROFILE["role"], GREEN, "400"),
    ("focus", PROFILE["focus"], CYAN, "400"),
    ("profile", PROFILE["handle"], MUTED, "400"),
]

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
    f'font-family="{FONT}">',
    '<style>'
    '@keyframes fadein{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}'
    '.static{display:none}'
    '.fade{opacity:0;animation:fadein .45s ease-out both}'
    '@media (prefers-reduced-motion: reduce){'
    '.fade{opacity:1!important;animation:none!important}'
    '.type{display:none}'
    '.static{display:inline}'
    '}'
    '</style>',
    f'<defs><linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
    f'<stop offset="0" stop-color="{BG2}"/><stop offset="1" stop-color="{BG}"/></linearGradient>'
    f'<linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">'
    f'<stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset="1" stop-color="{CYAN}"/>'
    '</linearGradient></defs>',
    f'<rect width="{W}" height="{H}" rx="12" fill="url(#bg)"/>',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="{FRAME}"/>',
    f'<line x1="0" y1="{TITLEBAR_H}" x2="{W}" y2="{TITLEBAR_H}" stroke="{FRAME}"/>',
]
for i, dot in enumerate(["#ff5f56", "#ffbd2e", "#27c93f"]):
    parts.append(f'<circle cx="{PAD + i*16}" cy="{TITLEBAR_H/2}" r="5" fill="{dot}"/>')
parts.append(f'<text x="{W/2}" y="{TITLEBAR_H/2 + 4}" fill="{MUTED}" font-size="12" '
             f'text-anchor="middle">{host}: ~$ whoami</text>')

# ---- typed whoami lines ---------------------------------------------------
y = TITLEBAR_H + PAD + 30
t = TYPE_START
for label, value, color, weight in lines:
    prefix = f"$ {label}: "
    px = PAD + 24 + len(prefix) * CH
    parts.append(typed(esc(prefix), PAD + 24, y, t, MUTED))
    parts.append(typed(esc(value), px, y, t + type_dur(esc(prefix)), color, weight))
    t += type_dur(esc(prefix)) + type_dur(esc(value)) + LINE_GAP
    y += LINE_H

y += 6
parts.append(f'<rect x="{PAD+24}" y="{y}" width="0" height="1" fill="url(#rule)" opacity="0.7">'
             f'<animate attributeName="width" from="0" to="{W - PAD*2 - 48}" '
             f'begin="{t:.2f}s" dur="0.5s" fill="freeze"/></rect>')
y += 34

# ---- "now" bullets --------------------------------------------------------
for item in PROFILE["now"]:
    t += 0.22
    bullet = "* "
    parts.append(typed(esc(bullet), PAD + 24, y, t, GOLD))
    parts.append(typed(esc(item), PAD + 24 + len(bullet) * CH, y, t + type_dur(esc(bullet)), INK))
    t += type_dur(esc(bullet)) + type_dur(esc(item))
    y += 34

y += 10
parts.append(f'<rect x="{PAD}" y="{y}" width="{W - PAD*2}" rx="10" fill="{TILE}" stroke="{FRAME}"/>')
y += 40
parts.append(typed(esc("$ cat stack.json"), PAD + 24, y, t, MUTED))
t += type_dur("$ cat stack.json")

# ---- skill chips ----------------------------------------------------------
CHIP_H = 34
for group, items in PROFILE["skills"]:
    y += 38
    t += 0.25
    parts.append(typed(esc(group), PAD + 24, y, t, CYAN, "700"))
    t += type_dur(esc(group))
    x = PAD + 24 + (len(group) + 2) * CH
    for name in items:
        w = (len(name) + 2) * CH + 8
        if x + w > W - PAD - 12:
            x = PAD + 24
            y += CHIP_H + 8
            t += 0.08
        parts.append(
            f'<g class="fade" style="animation-delay:{t:.2f}s">'
            f'<rect x="{x:.1f}" y="{y - 24}" width="{w:.1f}" height="{CHIP_H}" rx="17" '
            f'fill="{BG}" stroke="{FRAME}"/>'
            f'<circle cx="{x + 14:.1f}" cy="{y - 7:.1f}" r="4" fill="{GREEN}"/>'
            f'<text x="{x + 26:.1f}" y="{y - 1:.1f}" fill="{INK}" font-size="19">{esc(name)}</text></g>'
        )
        x += w + 8
        t += 0.06

# ---- contact lines --------------------------------------------------------
contact_y = max(y + 44, H - STATUS_H - PAD - 30 * len(PROFILE["links"]) + 10)
for key, value in PROFILE["links"]:
    t += 0.2
    label = f"$ {key}: "
    parts.append(typed(esc(label), PAD + 24, contact_y, t, MUTED))
    parts.append(typed(esc(value), PAD + 24 + len(label) * CH, contact_y, t + type_dur(esc(label)), CYAN))
    t += type_dur(esc(label)) + type_dur(esc(value))
    contact_y += 30

# ---- status bar -----------------------------------------------------------
sep_y = H - STATUS_H
parts.append(f'<line x1="0" y1="{sep_y}" x2="{W}" y2="{sep_y}" stroke="{FRAME}"/>')
status_y = sep_y + 19
status = f'{host}:~$ whoami {PROFILE["name"]} '
parts.append(f'<text x="{PAD}" y="{status_y}" fill="{MUTED}" font-size="13">{esc(status)}</text>')
parts.append(f'<rect x="{PAD + len(status) * 13 * 0.6:.1f}" y="{status_y - 12}" width="8" height="14" fill="{INK}">'
             f'<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.51;1" '
             f'dur="1s" repeatCount="indefinite"/></rect>')

parts.append("</svg>")
svg = "".join(parts)
svg = '<?xml version="1.0" encoding="UTF-8"?>\n' + svg
open(OUT, "w", encoding="utf-8").write(svg)
print(f"wrote {OUT}: {W} x {H}, {len(svg)//1024} KB, content bottom at y={contact_y:.0f}/{H - STATUS_H}")

