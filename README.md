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
- **`docs`**: Drawings and documentation
- **`kicad-library`**: Pinned KiCad library (submodule)
- **`scripts`**: Additional scripts for CI/CD
- **`watch`**: KiCad project for the watch
- **`CHANGELOG.md`**: Version history
- **`LICENSE`**: Project license (GPL-3.0)
- **`README.md`**: Project overview

The manufacturing outputs (Gerbers, BoM, documentation, etc.) are not part of the repository. They are
attached to each [release](https://github.com/ZSWatch/Watch-HW/releases) and published on GitHub Pages.

## Purchasing

TBD

## KiCad library

Initialize the pinned library after cloning:

```sh
git submodule update --init -- kicad-library
```

## Ressources

- [KiBot Template](https://github.com/nguyen-v/KDT_Hierarchical_KiBot)

## 👨‍💻 Maintainer

- [Daniel Kampert](mailto:danielkameprt@kampis-elektroecke.de)
