#!/usr/bin/env python3
"""Generate the homepage's inline mask from its canonical SVG asset."""

import argparse
from pathlib import Path
import sys
from urllib.parse import quote
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets/chess-wallpaper.svg"
OUTPUT = ROOT / "_includes/head/chess-wallpaper-inline.css"
SVG_NAMESPACE = "http://www.w3.org/2000/svg"


def render() -> str:
    """Remove nonvisual metadata and encode the same geometry as one CSS URL."""
    ET.register_namespace("", SVG_NAMESPACE)
    svg = ET.fromstring(SOURCE.read_bytes())
    if svg.tag != f"{{{SVG_NAMESPACE}}}svg":
        raise ValueError("Wallpaper must be an SVG document")
    for element in svg.iter():
        for name in list(element.attrib):
            if name.startswith("data-"):
                del element.attrib[name]
        if element.text is not None and not element.text.strip():
            element.text = None
        if element.tail is not None and not element.tail.strip():
            element.tail = None
    compact_svg = ET.tostring(svg, encoding="unicode", short_empty_elements=True)
    encoded_svg = quote(compact_svg, safe="/:=,.-_")
    return (
        "/* Generated from assets/chess-wallpaper.svg; regenerate with "
        "python3 scripts/generate-inline-wallpaper.py. */\n"
        f'--chess-wallpaper: url("data:image/svg+xml,{encoded_svg}");\n'
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Fail if the committed include is stale"
    )
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text() != expected:
            print(
                "Inline wallpaper is stale; run python3 scripts/generate-inline-wallpaper.py",
                file=sys.stderr,
            )
            return 1
        print("Inline wallpaper is current.")
        return 0
    OUTPUT.write_text(expected)
    print(f"Generated {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
