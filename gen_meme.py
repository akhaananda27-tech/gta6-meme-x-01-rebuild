#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Generate the GTA 6 meme for make.fun competition gta6-meme-x-01 (rebuild).

Concept (fresh, top-1 genre): a LEONIDA PUBLIC LIBRARY overdue notice.
GTA V was checked out on 17 Sep 2013 and is 4,801 days overdue. The fine is
itemised, and the whole thing is stamped PAID IN FULL by the patron's AI
agent on make.fun. Dense realistic document text, magenta make.fun ghost
worked into the stamp, high contrast, readable at phone size.

Deterministic: fixed dates, fixed layout, no network, no wall clock.
Output: meme.png (1080x1080) next to this script, or in $MEME_OUTPUT_DIR.
"""
import os
from datetime import date

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1080
OUT = os.environ.get("MEME_OUTPUT_DIR", os.path.dirname(os.path.abspath(__file__)))
PRESS = "/home/hatch/workspace/makefun/gta6-meme-x-01-kit/press/mark-1024.png"

# Fixed dates: GTA V out 17 Sep 2013, due back 1 Oct 2013, notice 23 Nov 2026.
DUE = date(2013, 10, 1)
NOTICE = date(2026, 11, 23)
DAYS = (NOTICE - DUE).days  # 4801
DAILY = 0.25
LATE_FEE = DAYS * DAILY            # 1200.25
SURCHARGE = 13.00                  # "waiting for the sequel" surcharge
DAMAGES = 999.99                   # emotional damages
TOTAL = LATE_FEE + SURCHARGE + DAMAGES  # 2213.24

INK = (26, 20, 24)
PAPER = (247, 242, 231)
PAPER_EDGE = (226, 214, 190)
RED = (178, 18, 30)
MAGENTA = (196, 0, 122)
DARK_BG = (24, 8, 28)
FAINT = (110, 98, 88)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text(draw, xy, s, f, fill=INK, anchor="la"):
    draw.text(xy, s, font=f, fill=fill, anchor=anchor)


def centre(draw, y, s, f, fill=INK, x=W // 2):
    draw.text((x, y), s, font=f, fill=fill, anchor="ma")


def rule(draw, y, x0=70, x1=W - 70, fill=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def money(v):
    return f"${v:,.2f}"


def main():
    img = Image.new("RGB", (W, H), DARK_BG)
    d = ImageDraw.Draw(img)

    # --- paper sheet -------------------------------------------------------
    d.rounded_rectangle([36, 28, W - 36, H - 28], radius=18, fill=PAPER,
                        outline=PAPER_EDGE, width=3)
    d.rounded_rectangle([48, 40, W - 48, H - 40], radius=12,
                        outline=(200, 186, 160), width=1)

    # --- header ------------------------------------------------------------
    centre(d, 52, "LEONIDA PUBLIC LIBRARY", font(SERIF, 44), INK)
    centre(d, 104, "101 Ocean Drive  •  Vice City, Leonida  •  EST. 1986",
           font(SANS, 21), FAINT)
    centre(d, 130, "\"WE NEVER FORGET.\"",
           font(SERIF_R, 20), FAINT)
    rule(d, 164)

    # --- red FINAL NOTICE banner -------------------------------------------
    d.rectangle([70, 180, W - 70, 232], fill=RED)
    centre(d, 190, "OVERDUE NOTICE  —  FINAL DEMAND", font(SANS_B, 34),
           (255, 255, 255))
    centre(d, 242, "Notice No. 000013  •  Issued 23 NOV 2026  •  Account: EVERY GTA FAN",
           font(MONO, 20), RED)

    # --- addressee block ----------------------------------------------------
    y = 272
    text(d, (70, y), "Dear PATRON #000013,", font(SANS_B, 26))
    y += 36
    lines = [
        "Our records show the item below was checked out",
        "13 YEARS AGO and has never been returned.",
    ]
    for ln in lines:
        text(d, (70, y), ln, font(SANS, 25))
        y += 30

    # --- item box ------------------------------------------------------------
    y += 6
    d.rounded_rectangle([70, y, W - 70, y + 140], radius=10,
                        outline=INK, width=2)
    text(d, (92, y + 12), "ITEM ON LOAN", font(MONO_B, 20), RED)
    text(d, (92, y + 40), "Grand Theft Auto V  (PlayStation 3)", font(SANS_B, 27))
    text(d, (92, y + 74),
         "Checked out: 17 SEP 2013      Due back: 01 OCT 2013",
         font(MONO, 21))
    text(d, (92, y + 104),
         f"Days overdue: {DAYS:,}  —  yes, {DAYS:,} days.",
         font(MONO_B, 21), RED)
    y += 156

    # --- itemised fines ------------------------------------------------------
    text(d, (70, y), "FINES OWED", font(SANS_B, 26))
    y += 34
    rule(d, y, width=1)
    y += 8
    rows = [
        ("Late fee — $0.25 / day  ×  4,801 days", money(LATE_FEE)),
        ("\"Waiting for the sequel\" surcharge", money(SURCHARGE)),
        ("Trailer 1 re-watched 847 times", "$0.00"),
        ("Emotional damages — 13 yrs of \"GTA 6 when?\"", money(DAMAGES)),
        ("Replacement copy: GTA VI (26 MAY 2026)", "PRICELESS"),
    ]
    for label, amount in rows:
        text(d, (70, y), label, font(SANS, 23))
        text(d, (W - 70, y), amount, font(MONO_B, 23), anchor="ra")
        y += 32
    rule(d, y + 2, width=1)
    y += 10
    text(d, (70, y), "TOTAL DUE", font(SANS_B, 30), RED)
    text(d, (W - 70, y), money(TOTAL), font(MONO_B, 32), anchor="ra", fill=RED)
    y += 44

    # --- PAID stamp (rotated) + make.fun ghost ------------------------------
    # Stamp sits bottom-right; footer text runs down the left beside it.
    stamp = Image.new("RGBA", (400, 180), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rounded_rectangle([6, 6, 394, 174], radius=14,
                         outline=MAGENTA, width=6)
    sd.text((200, 16), "PAID IN FULL", font=font(SANS_B, 44),
            fill=MAGENTA, anchor="ma")
    sd.text((200, 66), "BY MY AI AGENT", font=font(SANS_B, 28),
            fill=MAGENTA, anchor="ma")
    ghost = Image.open(PRESS).convert("RGBA").resize((72, 72))
    stamp.alpha_composite(ghost, (24, 98))
    sd.text((108, 104), "make.fun", font=font(SANS_B, 42),
            fill=MAGENTA, anchor="la")
    sd.text((108, 148), "agents win real money",
            font=font(SANS, 18), fill=MAGENTA, anchor="la")
    stamp = stamp.rotate(-6, expand=True, resample=Image.BICUBIC)
    stamp_top = y + 6
    img.paste(stamp, (W - 70 - stamp.width, stamp_top), stamp)

    # --- footer (left column, beside the stamp) ------------------------------
    rule(d, y, width=1)
    fy = y + 16
    text(d, (70, fy), "No further action required.", font(SANS_B, 24), INK)
    fy += 30
    text(d, (70, fy), "Keep GTA V — GTA VI arrives", font(SANS, 23), INK)
    fy += 26
    text(d, (70, fy), "26 MAY 2026.", font(SANS_B, 23), INK)
    fy += 32
    text(d, (70, fy), "Your AI agent can earn real", font(SANS, 22), FAINT)
    fy += 24
    text(d, (70, fy), "money too. Play at make.fun", font(SANS, 22), FAINT)
    # barcode (deterministic pattern from the account number)
    bx, by = 70, fy + 30
    code = "00001313371337"
    x = bx
    for i, ch in enumerate(code):
        wbar = 2 + (int(ch) % 3) * 2
        d.rectangle([x, by, x + wbar, by + 26], fill=INK)
        x += wbar + 3
    text(d, (70, by + 32), "LIBRARY CARD 0000 13 1337 1337", font(MONO, 15), FAINT)

    path = os.path.join(OUT, "meme.png")
    img.save(path, "PNG")
    print(f"wrote {path} {W}x{H} days={DAYS} total={money(TOTAL)}")


if __name__ == "__main__":
    main()
