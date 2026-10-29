# Changelog

## [Unreleased]

## [1.1.0] - 2026-10-29

**Added:**

- Test pads for FEM pins, so NORA-W126 (drop-in compatible, with FEM for higher output power) can be mounted instead of NORA-B106 (#21)
- Pads for speaker instead of a speaker connector (#18)
- Extra power test points on the bottom side of the board (#18)
- Mouser cart (CSV) for the BoM import and a check of the BoM against the schematic in the assembly outputs

**Changed:**

- Larger 1.25 mm pitch battery connector (Molex 53261-0271) (#18)
- Battery and speaker stickout reduced by 0.5 mm (#18)
- Optional speaker LS801 excluded from the board and BOM (#18)
- Project ported to KiCad 10 and updated to the latest KiCad template (KiBot configuration, CI/CD workflow, release skills)
- Manufacturing outputs are no longer committed to the repository, they are attached to the release and published on GitHub Pages

**Fixed:**

- Restore missing 3D models in previews and STEP exports, and correct release validation reports. PCB layout and electrical design unchanged (#24)

## [1.0.0] - 2026-02-21

**Added:**

- Initial release

[unreleased]: https://github.com/ZSWatch/Watch-HW/compare/1.1.0...HEAD
[1.1.0]: https://github.com/ZSWatch/Watch-HW/compare/1.0.0...1.1.0
[1.0.0]: https://github.com/ZSWatch/Watch-HW/compare/95d0aab8f4096c096bc494c76be4f3cb53c9ec07...1.0.0

**Full Changelog**:
https://github.com/ZSWatch/Watch-HW/compare/1.0.0...1.1.0
