> [!IMPORTANT]  
> This is a prototype right now, not fully tested. Do not order.
> Please use https://github.com/ZSWatch/Watch-DevKit-HW until this PCB is finalized.
> Not recommended to order the older legacy_zswatch. 

# ZSWatch-Watch

[![License](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](https://opensource.org/license/gpl-3-0/)

## 📑 Table of Contents

- [ZSWatch-Watch](#zswatch-watch)
  - [📑 Table of Contents](#-table-of-contents)
  - [📖 About](#-about)
  - [📂 Directory Breakdown](#-directory-breakdown)
  - [Purchasing](#purchasing)
  - [KiCad library](#kicad-library)
  - [Ressources](#ressources)
  - [👨‍💻 Maintainer](#-maintainer)

## 📖 About

The **ZSWatch-Watch** project provides the hardware design and production files for a smartwatch development board tailored to the ZSWatch ecosystem.
It is built with **KiCad** and integrates a full **CI/CD pipeline** using **KiBot**, ensuring reproducible outputs for documentation, manufacturing, and releases.

Key features:

- 🛠️ Open-source hardware design
- 📦 Automated generation of Gerber, BoM, and documentation via KiBot
- 🔄 Workflow stages (DRAFT → PRELIMINARY → CHECKED → RELEASED) for structured releases
- 📝 Clear documentation and changelog to track progress
- 🌍 Designed with collaboration and transparency in mind

Please check the [wiki](https://github.com/ZSWatch/ZSWatch/wiki) for more information about the project.

You can also view this project on [CADLAB.io](...). 

## 📂 Directory Breakdown

- **`.github`**: GitHub related files
- **`.gitignore`**: Ignored files list
- **`devkit`**: KiCad project for the devkit
- **`production`**: Manufacturing outputs (Gerbers, documentation, etc.)
- **`CHANGELOG.md`**: Version history
- **`LICENSE`**: Project license (GPL-3.0)
- **`README.md`**: Project overview

## Purchasing

TBD

## KiCad library

Kampi's symbols, footprints, and 3D models are stored in the `kicad-library`
Git submodule. Git records its exact commit alongside the board design; CI
does not fetch the latest library version automatically.

After cloning Watch-HW, or after pulling a change to the library version, run
this command from the repository root:

```sh
git submodule update --init -- kicad-library
```

The initial library revision is `e78be312e017463be06bc1b227d8ba26fa0384dc`
(19 February 2026), reconstructed from the library history at the 1.0.0 release.
The original CI logs have expired, so the exact revision used then could not
be confirmed directly.

The project library tables and existing PCB model paths use the submodule
relative to `${KIPRJMOD}`. To ensure that models referenced inside newly
imported library footprints also use this checkout, launch KiCad with
`KICAD_LIBRARY` set to its absolute path:

```sh
KICAD_LIBRARY="$PWD/kicad-library" kicad watch/ZSWatch-Watch.kicad_pro
```

Alternatively, set `KICAD_LIBRARY` to this repository's `kicad-library` directory
in KiCad's **Preferences → Configure Paths**. `watch/kibot_launch.sh` sets the
variable automatically for local KiBot runs. CI logs the library revision.

To intentionally update the library, select a reviewed commit and test the
board before recording the new submodule revision:

```sh
git -C kicad-library fetch origin
git -C kicad-library checkout --detach <reviewed-commit>
# Verify the schematic, footprints, and 3D renders, then:
git add kicad-library
```

## Ressources

- [KiBot Template](https://github.com/nguyen-v/KDT_Hierarchical_KiBot)

## 👨‍💻 Maintainer

- [Daniel Kampert](mailto:danielkameprt@kampis-elektroecke.de)
