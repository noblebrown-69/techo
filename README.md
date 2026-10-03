# 手帳 Techo

Techo is a plain, tabbed text editor for BushidOS. It is a faithful fork of
[Xed](https://github.com/linuxmint/xed), the text editor from Linux Mint, and stays as close to it as possible.
Techo is released under the GPL-2.0-or-later, like Xed. All credit for the editor itself goes to the Xed,
Pluma and gedit authors.

Techo installs side by side with xed: the binary is `techo`, the app id is `org.bushidos.Techo`, and its
settings live under `org.bushidos.Techo` (GSettings) and `~/.config/techo`.

Build and install for the current user:

    meson setup build --prefix=$HOME/.local
    ninja -C build && ninja -C build install

---

*Original Xed README follows.*

# Xed Text Editor
![build](https://github.com/linuxmint/xed/actions/workflows/build.yml/badge.svg)

xed is a small and lightweight text editor.

xed supports most standard editing features, plus several not found in your
average text editor (plugins being the most notable of these).

Although new features are always under development, currently xed has:

    * Complete support for UTF-8 text
    * Syntax highlighting
    * Support for editing remote files
    * Search and Replace
    * Printing and Print Previewing Support
    * File Revert
    * A complete preferences interface
    * Configurable Plugin system, with optional python support

Some of the plugins, packaged and installed with xed include, among others:

    * Change Case
    * Document Statistics
    * File Browser
    * Indent Lines
    * Insert Date/Time
    * Modelines
    * Save Without Trailing Spaces
    * Sort
    * Spell checker
    * Tag list
    * Word Completion


## Installation

```
    1. run the 'configure' script
      # meson --prefix=/usr build
    2. build xed
      # ninja -v -C build
    3. install xed
      # sudo ninja install -v -C build

    ** Build Instructions for Debian-based distros **
    1. run "dpkg-buildpackage" from the xed base directory
    2. cd ..
    3. run 
      # sudo dpkg -i *.deb
    4. From then, any new changes can be applied by running
      # sudo ninja -C debian/build install 
```

### Xed look and feel

##### Classic Mode
![classic-screenshot](/screencaptures/classic_screencapture.png?raw=true)

##### Theme selections
![theme-screenshot](/screencaptures/theme_screencapture.png?raw=true)

##### Search and Replace feature
![search-replace-screenshot](/screencaptures/search_replace_screencapture.png?raw=true)

##### Select from several languages in Highlight syntax mode
![highlightmode-screenshot](/screencaptures/highlightmode_screencapture.png?raw=true)

##### Xed Shortcuts
![shortcuts-1-screenshot](/screencaptures/shortcuts_1_screencapture.png?raw=true)
![shortcuts-2-screenshot](/screencaptures/shortcuts_2_screencapture.png?raw=true)



> xed is released under the GNU General Public License (GPL) version 2, see
> the file 'COPYING' for more information.
