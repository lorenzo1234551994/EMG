#!/usr/bin/env python3
"""
Genera le icone dell'app (raggio elettrico) in tutte le misure richieste.
Per cambiare i colori basta modificare BG e BOLT qui sotto e rilanciare lo script.
"""
from PIL import Image, ImageDraw
import os

# ---- palette: cambia solo queste due righe -------------------------------
BG   = "#0F201C"   # sfondo del riquadro
BOLT = "#0E7C66"   # raggio
# --------------------------------------------------------------------------

OUT = "/mnt/user-data/outputs"
SS = 8  # supersampling: disegna in grande e riduce, per bordi puliti

# raggio elettrico, coordinate normalizzate 0-1 (y verso il basso)
BOLT_PATH = [
    (0.600, 0.040), (0.205, 0.560), (0.435, 0.560),
    (0.400, 0.960), (0.795, 0.440), (0.565, 0.440),
]


def draw_icon(size, pad=0.0, radius_ratio=0.22, transparent_bg=False):
    """pad = margine interno in frazione del lato (per le icone maskable)."""
    S = size * SS
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    if not transparent_bg:
        if radius_ratio > 0:
            d.rounded_rectangle([0, 0, S - 1, S - 1],
                                radius=int(S * radius_ratio), fill=BG)
        else:
            d.rectangle([0, 0, S - 1, S - 1], fill=BG)

    # il raggio occupa l'area centrale, ridotta dal padding
    inner = S * (1 - 2 * pad)
    off = S * pad
    pts = [(off + x * inner, off + y * inner) for x, y in BOLT_PATH]
    d.polygon(pts, fill=BOLT)

    return img.resize((size, size), Image.LANCZOS)


def main():
    os.makedirs(OUT, exist_ok=True)
    made = []

    # icone standard (angoli arrotondati, il raggio riempie il riquadro)
    for size in (192, 512):
        p = f"{OUT}/icon-{size}.png"
        draw_icon(size, pad=0.14).save(p)
        made.append(p)

    # icona maskable: sfondo pieno e soggetto dentro la zona sicura del 40%
    for size in (192, 512):
        p = f"{OUT}/icon-{size}-maskable.png"
        draw_icon(size, pad=0.26, radius_ratio=0).save(p)
        made.append(p)

    # iOS: nessun angolo arrotondato, li aggiunge il sistema
    p = f"{OUT}/apple-touch-icon.png"
    draw_icon(180, pad=0.16, radius_ratio=0).save(p)
    made.append(p)

    # favicon
    p = f"{OUT}/favicon.png"
    draw_icon(64, pad=0.10, radius_ratio=0.18).save(p)
    made.append(p)

    for f in made:
        print(os.path.basename(f), os.path.getsize(f), "byte")


if __name__ == "__main__":
    main()
