#!/usr/bin/env python3
"""Reproduce responsive homepage images and inline profile icons.

Requires Pillow 9.1+ with WebP support (python3 -m pip install Pillow).
Run: python3 scripts/optimize-homepage-images.py
Use --check to verify the committed derivatives; a JSON manifest is printed.
"""

import argparse
from base64 import b64encode
import hashlib
from io import BytesIO
import json
from pathlib import Path
import sys
from typing import Optional

from PIL import Image, ImageOps, __version__ as PILLOW_VERSION, features

ROOT = Path(__file__).resolve().parents[1]
PROFILE_ICON_DATA = ROOT / "_data/profile_icons.json"
PUBLICATION_ARTWORK = ROOT / "assets/publication-artwork"
THUMBNAILS = (
    "thumb-binprop.png",
    "thumb-caddie.png",
    "thumb-algotune.png",
    "thumb-humanitysexam.png",
    "thumb-swebench.png",
    "thumb-citeme.png",
    "thumb-entropy.png",
    "thumb-rdumb.png",
    "thumb-calibrated.png",
    "thumb-emerging.png",
)
SOCIAL_ICONS = (
    "email-icon.png",
    "twitter-icon.png",
    "googlescholar-icon.png",
    "github-icon.png",
    "linkedin-icon.png",
)
THUMBNAIL_SIZES = (160, 320, 480)
THUMBNAIL_INSET = 0.08
PORTRAIT_WIDTHS = (240, 336, 480, 648, 800)
THUMBNAIL_QUALITY = 92
PORTRAIT_QUALITY = 84


def encode(image: Image.Image, format_name: str, quality: Optional[int]) -> bytes:
    output = BytesIO()
    if format_name == "WEBP":
        if quality is None:
            image.save(output, "WEBP", lossless=True, method=6, exact=True)
        else:
            image.save(output, "WEBP", quality=quality, method=6)
    else:
        image.save(output, "PNG", optimize=True, compress_level=9)
    data = output.getvalue()
    with Image.open(BytesIO(data)) as decoded:
        if decoded.size != image.size:
            raise ValueError("Encoded derivative changed its dimensions")
        if quality is None and decoded.convert("RGBA").tobytes() != image.convert("RGBA").tobytes():
            raise ValueError("Encoded derivative changed its prepared image pixels")
        if quality is not None and "A" in image.getbands():
            if decoded.convert("RGBA").getchannel("A").tobytes() != image.getchannel("A").tobytes():
                raise ValueError("Encoded derivative changed its transparency")
    return data


def derivatives():
    for name in THUMBNAILS:
        source = PUBLICATION_ARTWORK / name
        with Image.open(source) as original:
            image = original.convert("RGBA")
            for size in THUMBNAIL_SIZES:
                inset = round(size * THUMBNAIL_INSET)
                artwork = ImageOps.contain(image, (size - 2 * inset,) * 2, Image.Resampling.LANCZOS)
                square = Image.new("RGB", (size, size), "white")
                position = ((size - artwork.width) // 2, (size - artwork.height) // 2)
                square.paste(artwork, position, artwork)
                target = ROOT / "assets/optimized" / f"{source.stem}-{size}.webp"
                yield source, target, square, "WEBP", THUMBNAIL_QUALITY
    source = ROOT / "images/neckar.jpeg"
    with Image.open(source) as original:
        for width in PORTRAIT_WIDTHS:
            height = round(original.height * width / original.width)
            portrait = original.resize((width, height), Image.Resampling.LANCZOS)
            target = ROOT / "images/optimized" / f"{source.stem}-{width}.webp"
            yield source, target, portrait, "WEBP", PORTRAIT_QUALITY
    for name in SOCIAL_ICONS:
        source = ROOT / "images" / name
        with Image.open(source) as original:
            image = original.convert("RGBA")
            image.thumbnail((80, 80), Image.Resampling.LANCZOS)
            target = ROOT / "images/optimized" / f"{source.stem}.webp"
            yield source, target, image, "WEBP", None
    source = ROOT / "images/algotune-mascot.png"
    with Image.open(source) as original:
        for size in (32, 192):
            image = original.convert("RGBA").resize(
                (size, size), Image.Resampling.LANCZOS
            )
            target = ROOT / "images/optimized" / f"favicon-{size}.png"
            yield source, target, image, "PNG", None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing files")
    args = parser.parse_args()
    records = []
    stale = []
    profile_icons = {}
    for source, target, image, format_name, quality in derivatives():
        data = encode(image, format_name, quality)
        if source.name in SOCIAL_ICONS:
            name = source.stem.removesuffix("-icon")
            profile_icons[name] = "data:image/webp;base64," + b64encode(data).decode("ascii")
        if args.check:
            if not target.exists() or target.read_bytes() != data:
                stale.append(str(target.relative_to(ROOT)))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        records.append(
            {
                "source": str(source.relative_to(ROOT)),
                "output": str(target.relative_to(ROOT)),
                "width": image.width,
                "height": image.height,
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "pixels_preserved_after_encoding": quality is None,
            }
        )
    inline_data = json.dumps(profile_icons, indent=2) + "\n"
    if args.check:
        if not PROFILE_ICON_DATA.exists() or PROFILE_ICON_DATA.read_text() != inline_data:
            stale.append(str(PROFILE_ICON_DATA.relative_to(ROOT)))
    else:
        PROFILE_ICON_DATA.write_text(inline_data)
    print(
        json.dumps(
            {
                "pillow_version": PILLOW_VERSION,
                "webp_version": features.version("webp"),
                "stale_outputs": stale,
                "outputs": records,
            },
            indent=2,
        )
    )
    if stale:
        print("Run python3 scripts/optimize-homepage-images.py to refresh derivatives.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
