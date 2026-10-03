#!/usr/bin/python3
# Copyright (C) 2026 Noble Brown
# SPDX-License-Identifier: GPL-2.0-or-later
"""Render the Techo app icon SVG to PNG sizes for hicolor."""
import os
import sys

import gi
gi.require_version("Rsvg", "2.0")
from gi.repository import Rsvg
import cairo

SIZES = [16, 22, 24, 32, 48, 64, 128, 256]


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    svg_path = os.path.join(here, "hicolor", "scalable", "apps", "org.bushidos.Techo.svg")
    handle = Rsvg.Handle.new_from_file(svg_path)
    if handle is None:
        print(f"error: could not load {svg_path}", file=sys.stderr)
        return 1
    for n in SIZES:
        out_dir = os.path.join(here, "hicolor", f"{n}x{n}", "apps")
        os.makedirs(out_dir, exist_ok=True)
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, n, n)
        ctx = cairo.Context(surface)
        rect = Rsvg.Rectangle()
        rect.x = 0
        rect.y = 0
        rect.width = n
        rect.height = n
        handle.render_document(ctx, rect)
        out_path = os.path.join(out_dir, "org.bushidos.Techo.png")
        surface.write_to_png(out_path)
        print(out_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
