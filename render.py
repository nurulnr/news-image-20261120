#!/usr/bin/env python3
"""Render the 20 November 2026 world-news front page (1024x1024 PNG).

Build tool only: the entry itself is a Node program that copies the
rendered entry.png to /output/entry.png. Deterministic: no timestamps,
no randomness, fixed layout.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = "/home/hatch/workspace/makefun/news-image-20261120-entry/entry.png"

PAPER = (247, 242, 231)      # newsprint cream
INK = (18, 18, 18)           # near-black
RED = (155, 27, 30)          # masthead / lead accent
GREY = (90, 86, 78)
RULE = (40, 40, 40)
BLUE = (28, 68, 128)
TEAL = (14, 110, 110)
GREEN = (28, 110, 52)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def flag_russia(draw, x, y, w, h):
    third = h / 3
    draw.rectangle([x, y, x + w, y + third], fill=(255, 255, 255))
    draw.rectangle([x, y + third, x + w, y + 2 * third], fill=(0, 57, 166))
    draw.rectangle([x, y + 2 * third, x + w, y + h], fill=(213, 0, 50))
    draw.rectangle([x, y, x + w, y + h], outline=(120, 120, 120), width=1)


def flag_poland(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h / 2], fill=(255, 255, 255))
    draw.rectangle([x, y + h / 2, x + w, y + h], fill=(220, 20, 60))
    draw.rectangle([x, y, x + w, y + h], outline=(120, 120, 120), width=1)


def flag_ukraine(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h / 2], fill=(0, 91, 187))
    draw.rectangle([x, y + h / 2, x + w, y + h], fill=(255, 213, 0))
    draw.rectangle([x, y, x + w, y + h], outline=(120, 120, 120), width=1)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # frame
    d.rectangle([14, 14, W - 15, H - 15], outline=INK, width=3)
    d.rectangle([20, 20, W - 21, H - 21], outline=INK, width=1)

    # ---- masthead ----
    f_mast = font(SERIF_B, 96)
    d.text((W / 2, 34), "THE WORLD", font=f_mast, fill=INK, anchor="ma")
    d.line([90, 138, W - 90, 138], fill=RULE, width=3)
    f_date = font(SANS_B, 33)
    d.text((W / 2, 150), "FRIDAY  ·  20 NOVEMBER 2026", font=f_date, fill=RED, anchor="ma")
    d.line([90, 196, W - 90, 196], fill=RULE, width=2)

    # ---- lead story ----
    lx, lw = 52, 600
    f_kick = font(SANS_B, 23)
    d.text((lx, 214), "NATO TERRITORY HIT", font=f_kick, fill=RED)
    f_head = font(SERIF_B, 42)
    head = wrap(d, "RUSSIAN MISSILES LAND IN POLAND",
                f_head, lw)
    y = text_block(d, lx, 246, head, f_head, INK, 48)
    f_sum = font(SANS, 22)
    summ = ("Poland says two Russian missiles landed in the south-east "
            "as Moscow's massive strikes hit Kyiv's bridges, killing 8.")
    y = text_block(d, lx, y + 8, wrap(d, summ, f_sum, lw), f_sum, INK, 29)

    # lead visual: three flags with labels
    vx, vw, vh = 700, 272, 64
    vy = 210
    for (fn, label) in ((flag_russia, "RUSSIA"), (flag_poland, "POLAND"), (flag_ukraine, "UKRAINE")):
        fn(d, vx, vy, vw, vh)
        d.rectangle([vx, vy, vx + vw, vy + vh], outline=(110, 110, 110), width=1)
        f_lab = font(SANS_B, 18)
        d.text((vx + vw / 2, vy + vh + 5), label, font=f_lab, fill=GREY, anchor="ma")
        vy += vh + 26

    d.line([52, 500, W - 52, 500], fill=RULE, width=2)

    # ---- story grid: 2 cols x 3 rows ----
    gx, gy = 52, 518
    cw, ch, gapx, gapy = 452, 138, 16, 12
    stories = [
        ("INDIA", RED, "CYCLONE AKVAN HITS INDIA'S EAST COAST",
         "Akvan made landfall near Gopalpur with 70–80 kmph winds — "
         "the third cyclone in a month."),
        ("MARKETS", GREEN, "ASIAN STOCKS SLIDE",
         "Nikkei fell 4.8% and SoftBank plunged 16% as the AI sell-off "
         "spread to Asia."),
        ("BERLIN", BLUE, "ALLIES MEET IN BERLIN, TALK TO RUSSIA",
         "Envoys discussed NATO-style security guarantees for Kyiv as "
         "Europe seeks a deal."),
        ("THE GULF", RED, "SAUDI INTERCEPTS MORE HOUTHI MISSILES",
         "Riyadh shot down missiles and drones a day after a Houthi strike "
         "damaged its PIF tower."),
        ("TECH", TEAL, "GTA 6 LAUNCH TOPS $2.3BN IN SALES",
         "Rockstar's Grand Theft Auto VI took $2.3bn in its first day on "
         "sale, a record for the series."),
        ("ALSO TODAY", GREY, "IN BRIEF",
         "Estonia shuts its Russia border for 6 months. · Kenya's last "
         "Ebola patient goes home. · IMF: debt nears 100% of GDP. · Youth "
         "strike in 25+ nations."),
    ]
    for i, (kick, col, head, body) in enumerate(stories):
        cx = gx + (i % 2) * (cw + gapx)
        cy = gy + (i // 2) * (ch + gapy)
        d.text((cx, cy), kick, font=font(SANS_B, 20), fill=col)
        f_h = font(SERIF_B, 25)
        hl = wrap(d, head, f_h, cw)
        yy = text_block(d, cx, cy + 26, hl, f_h, INK, 29)
        f_b = font(SANS, 18)
        bl = wrap(d, body, f_b, cw)
        text_block(d, cx, yy + 4, bl, f_b, INK, 23)

    # ---- footer ----
    d.line([90, 968, W - 90, 968], fill=RULE, width=2)
    d.text((W / 2, 976), "The world in one image  ·  Friday, 20 November 2026",
           font=font(SANS, 20), fill=GREY, anchor="ma")

    img.save(OUT, format="PNG", optimize=True)
    print("saved", OUT)


if __name__ == "__main__":
    main()
