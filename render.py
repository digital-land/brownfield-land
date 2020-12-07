#!/usr/bin/env python3

import sys

from digital_land_frontend.render import Renderer

if __name__ == "__main__":
    url_root = None  # default to name
    if len(sys.argv) > 1 and sys.argv[1] == "--local":
        url_root = "/"

    renderer = Renderer("brownfield land", "data/dataset.csv", url_root)
    renderer.render_pages()
