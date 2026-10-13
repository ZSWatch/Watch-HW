#!/usr/bin/env python3
"""Check the PCB's Kampi model paths before generating production outputs."""

from pathlib import Path
import re
import sys


def main():
    project_dir = Path(__file__).resolve().parents[2]
    library_dir = project_dir.parent / "kicad-library"
    if not (library_dir / "3D").is_dir():
        print(
            "KiCad library is not initialized. From the Watch-HW repository, run:\n"
            "  git submodule update --init -- kicad-library",
            file=sys.stderr,
        )
        return 1

    board = project_dir / "ZSWatch-Watch.kicad_pcb"
    prefixes = ("${KIPRJMOD}/../kicad-library/", "${KICAD_LIBRARY}/")
    model_paths = set()
    for model in re.findall(r'\(model\s+"([^"]+)"', board.read_text()):
        for prefix in prefixes:
            if model.startswith(prefix):
                model_paths.add(model[len(prefix):])
                break

    missing = sorted(path for path in model_paths if not (library_dir / path).is_file())
    if missing:
        print("Missing models in the pinned KiCad library:", file=sys.stderr)
        for path in missing:
            print(f"  {path}", file=sys.stderr)
        return 1

    print(f"Checked {len(model_paths)} Kampi 3D model files: all exist.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
