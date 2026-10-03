# 手帳 Techo: handoff

Times are PT (America/Phoenix, UTC-7). Supervisor: Donald (Grok Bot). Coder: Turing (Hermes `coding` profile, local Huihui Qwen3.8-27B on Aegis :8089).
Last updated: Oct 3, 2026 ~11:00 AM PT. Deployed to Lenovo + WD (~/.local, from tarball techo-local-0df57d8) and Techo is the default text editor on Aegis, Lenovo and WD. Nothing pushed.

## Hard rule for every session
Yūkan (nightly GPU job) runs 1:45 to about 5:00 AM PT and shares the GPU and llama with Turing.
No Turing requests from 1:40 AM PT until Yūkan is done. Check `date` before every request; don't start a long one after 1:30.

## Repo
- Work dir: `~/Dropbox/Development/Techo` on Aegis. Clone of https://github.com/linuxmint/xed at tag 3.9.0 (9be0bdc).
- Remote `upstream` = linuxmint/xed. No other remotes. Nothing has been pushed. Work branch: `techo`.
- Briefs and Turing's replies: `.techo-briefs/` (excluded via .git/info/exclude, not committed).

## Build deps (Aegis): ONE apt command for Noble
DONE: Noble ran this on Oct 3 morning. Kept for reference (other build machines):

    sudo apt install meson libgtksourceview-4-dev libxapp-dev libpeas-dev libgspell-1-dev libxml2-dev intltool itstool yelp-tools gobject-introspection libgirepository1.0-dev python-gi-dev

(Already present: ninja-build, libgtk-3-dev, libglib2.0-dev, libx11-dev, gettext, libxml2-utils, desktop-file-utils, and the runtime libs plus the system xed.)
Turing's pip meson was removed Oct 3 ~10:33 AM PT (`python3.14 -m pip uninstall -y meson`, Hermes' Python); `which meson` is /usr/bin/meson 1.3.2.

## Rebrand decisions (keep these)
- Renamed (installed or user-visible): binary `techo`; app id / D-Bus `org.bushidos.Techo`; desktop file `org.bushidos.Techo.desktop` (Name=手帳 Techo, StartupWMClass=techo); GSettings `org.bushidos.Techo.*` at `/org/bushidos/techo/`; gettext domain `techo`; `share/techo`, `lib/techo` (libxed.so + plugins + Xed-1.0.typelib), `include/techo`, `techo.pc`; help `help/C/techo`; man `techo.1`; user dirs `~/.config/techo`, `~/.cache/techo`, `~/.local/share/techo`.
- NOT renamed, on purpose (stay close to upstream so merges from linuxmint/xed stay easy): C file names, C identifiers (xed_*, XedWindow), the library name libxed (installed in a private techo dir), GIR namespace `Xed`, GResource paths `/org/x/editor/...`, CSS classes `.xed-window` etc., help page content, po translations content.
- So `grep -ri xed` still matches a lot of internal code. The real check is that no installed path, app id, schema id, or user-visible string says xed, except credits and upstream links.
- Document window titles behave like Xed ("name (dir)"); the empty window shows "手帳 Techo".

## Phase status
- Phase 1 (clone + deps): DONE. Clone at tag 3.9.0, `upstream` remote, branch `techo`. Deps missing on Aegis (apt command above). Stock xed baseline built OK on the box.
- Phase 2 (rebrand): DONE, 3 commits on `techo`:
  - f62a97e build system and data files (Turing; man page + StartupWMClass finished by Donald after Turing's fix round timed out)
  - f962331 C string ids: app id, schema ids, user/data dirs, window title, help name (Turing)
  - b9f8409 About dialog (手帳 Techo, "A fork of Xed by Linux Mint", GPL-2.0, copyright for Techo plus Xed/Pluma/gedit authors) and README credits (Turing)
  - Verified on the box: meson setup + ninja + install OK, desktop file validates, `techo` runs under Xvfb: window "手帳 Techo", WM_CLASS techo/Techo, a tab "Unsaved Document 1", no GSettings errors. Every installed path is techo-private or org.bushidos.Techo (only data/xed.xml still went to share/gtksourceview-4/styles; fixed in phase 3a).
- Phase 3 (theming): DONE. Commits (oldest first):
  - 4f6a18d `data/styles/bushidos-neon.xml` and `bushidos-classic.xml`, using exact hex values from BushidOS `src/gtk3/_colors-neon.scss` and `_colors.scss`. Installed to `share/techo/styles` (xed.xml moved there too) and added to the scheme search path.
  - aad3f2d default `scheme` = `'bushidos-auto'`: GTK theme `BushidOS-Neon*` gives bushidos-neon, `BushidOS*` gives bushidos-classic, anything else gives xed. Re-resolves live on `notify::gtk-theme-name`.
  - 147d6c0 Preferences shows the resolved scheme and no longer overwrites `bushidos-auto` when it opens (upstream connected the signal before setting the chooser).
  - Verified on the box under Xvfb with the real BushidOS themes: Neon and Classic both auto-select the right scheme (screenshots below). Opening Preferences does not write a `scheme` key.
  - c012074 strings pass: user-visible "xed" changed to "Techo" in C translatable strings, gschema descriptions, the modelines plugin and the matching po entries. Python plugins use gettext domain `techo`. The 8 po files that fail `msgfmt -c` (ab be ga mai mg ms sr sr@latin) already failed upstream.
  - 287902b Preferences > Theme: "Follow the BushidOS theme" switch. On writes `bushidos-auto` and locks the scheme list; off writes the chooser's scheme. Turing's first version had the wrong notify-handler signature (crashed with criticals in my test). Fixed after one review round, then verified on Xvfb: off gives `scheme='bushidos-neon'`, on gives `scheme='bushidos-auto'`, 0 CRITICALs.
  - ca74a87 the follow switch now sits directly under "Use dark theme variant" (packing positions fixed). Verified on Xvfb (Classic): row in place, BushidOS Classic auto-selected, 0 CRITICALs.
- Build state: code at e7f90c1 (help docs after ca74a87). A clean `git archive` build on the box at 1:07 AM: meson setup, ninja (0 errors) and install all pass; desktop-file-validate and `glib-compile-schemas --strict` pass. No installed path names xed outside techo-private dirs. Runs under Xvfb.
- Phase 4 (install to ~/.local on Aegis, launch, screenshot): DONE Oct 3 ~10:35 AM PT.
  - Out-of-tree build dir so artifacts don't sync through Dropbox: `meson setup ~/.cache/techo-build --prefix=$HOME/.local && ninja -C ~/.cache/techo-build && ninja -C ~/.cache/techo-build install` (logs in `~/.cache/techo/{setup,build,install}.log`). 0 errors. Rebuild: just `ninja -C ~/.cache/techo-build install`.
  - Schemas: the post-install script compiles `~/.local/share/glib-2.0/schemas/gschemas.compiled`; `gsettings list-schemas` finds all 16 `org.bushidos.Techo*` with no env vars (GLib already searches ~/.local/share). No XDG_DATA_DIRS / GSETTINGS_SCHEMA_DIR override in the launcher.
  - Desktop file `~/.local/share/applications/org.bushidos.Techo.desktop` validates; `update-desktop-database ~/.local/share/applications` run. Techo is listed as a text/plain handler; mimeapps.list defaults not changed.
  - Live launch on :0 with 3 tabs (sample.c, hello.py, notes.txt from `~/.cache/techo/test/`): WM_CLASS techo/Techo, BushidOS-Neon chrome + bushidos-neon scheme auto-selected. Screenshots: `~/.cache/techo/shots/aegis-live.png` (before icon) and `aegis-live-icon.png` (with the new icon); copies on the box at `/workspace/techo/`. Test windows closed. Only log line: the BushidOS theme's own "gtk.css:1:0 unknown @ rule" warning.
  - Live theme-follow test NOT run on Aegis: it would mean toggling Noble's real theme, and Aegis has no Xvfb/xsettingsd for an isolated session. The resolver is unit-verified on the box under Xvfb per theme; live re-resolve on `notify::gtk-theme-name` is still untested end-to-end. Test it when Noble next switches themes himself, or on the box with xsettingsd.
- Phase 5 (app icon): DONE.
  - b39636d `data/icons/hicolor/scalable/apps/org.bushidos.Techo.svg` (original art: pocket notebook, magenta spine, cyan band and ruled lines, vermilion hanko seal with a stylised 手 path, gold bookmark ribbon; Neon palette; no text/fonts) + PNGs 16/22/24/32/48/64/128/256 rendered by `data/icons/render-pngs.py` (gi Rsvg + pycairo, /usr/bin/python3).
  - 10e09de desktop `Icon=org.bushidos.Techo`, About `logo_icon_name`, `gtk_window_set_default_icon_name`; meson installs the hicolor icons; new DESTDIR-guarded `install-scripts/meson_install_icons.py` runs `gtk-update-icon-cache -q -t -f` on `$prefix/share/icons/hicolor` (this created a user `~/.local/share/icons/hicolor/icon-theme.cache`, which indexes all icons there, including the other apps'). Verified: Gtk.IconTheme resolves the icon at 16/48/256, the window has a 32x32 _NET_WM_ICON, and the titlebar shows it.
  - Possible follow-up: a Classic-palette variant or a symbolic icon.
- Screenshots (box, Xvfb, real BushidOS GTK themes), in `.techo-briefs/`: `box-xvfb-neon.png` (Neon chrome + bushidos-neon scheme, auto), `box-xvfb-classic.png` (Classic + bushidos-classic, auto), `box-xvfb-about-neon.png` (About dialog), `box-xvfb-prefs-classic.png` (Preferences > Theme with the follow switch).

## Runtime deps (for packaging to the laptops later; NOT deployed)
`ldd` of `~/.local/bin/techo` + `lib/x86_64-linux-gnu/techo/libxed.so` resolves 82 libs, none missing; the only non-system one is Techo's own libxed.so. Direct packages (Mint 22.3 / Ubuntu 24.04 names):
- Core: libgtk-3-0t64, libglib2.0-0t64, libgtksourceview-4-0 (4.8.4), libxapp1 (3.2.3+zena) + xapps-common, libpeas-1.0-0 (1.36.0; also ships the python3 loader `libpeas-1.0/loaders/libpython3loader.so`), libgirepository-1.0-1, libxml2, libx11-6, libpango-1.0-0, libcairo2, libgdk-pixbuf-2.0-0, libatk1.0-0t64, libc6.
- Plugins (spell): libgspell-1-2, libenchant-2-2.
- Python plugins (2 python3 loaders, 1 C): python3, python3-gi, gir1.2-gtk-3.0, gir1.2-gtksource-4, gir1.2-peas-1.0, gir1.2-xapp-1.0; Techo ships its own Xed-1.0.typelib.
- Data/other: iso-codes (encodings), yelp (F1 help), gsettings-desktop-schemas (pulled in by gtk).
- The rest are transitive (pulled by the above): xcb/X11 ext libs, wayland client libs, harfbuzz/freetype/fontconfig, libxklavier16/libgnomekbd8 (via libxapp), icu74, etc.
- This matches stock `xed`'s Depends list, so `apt install xed` on a laptop also pulls every runtime dep. Package plan: a .deb built with `meson setup --prefix=/usr` (DESTDIR install skips the post-install scripts; dpkg triggers handle schemas, icons and desktop db).

## Deployment (Oct 3, ~10:53-10:57 AM PT, at Noble's request)
- Package: `DESTDIR=/tmp/techo-stage ninja -C ~/.cache/techo-build install`, tarred from the staged `home/franklin/.local` (include/ and pkgconfig left out) as `dist/techo-local-0df57d8.tar.gz` (5.0 MB, sha256 a2d6649d…8954; `dist/` is git-excluded). Paths are baked to /home/franklin/.local (franklin on every machine).
- Moved via the box (Lenovo's Dropbox doesn't have Development/Techo; WD's Dropbox isn't syncing): CopyToBox, then CopyFromBox to `~/techo-local-0df57d8.tar.gz` on each laptop. Checksums match.
- Laptops (Mint 22.3, glibc 2.39, same as Aegis): extracted into ~/.local; glib-compile-schemas, gtk-update-icon-cache -t, update-desktop-database; desktop file validates; 16 schemas, scheme 'bushidos-auto'. `ldd`: nothing missing for the binary, libxed or the plugins; every runtime package is present (xed 3.8.9+zena installed on both). **No apt command needed.**
- Defaults (all 3 machines, `~/.config/mimeapps.list`, backup `mimeapps.list.bak-20261003`; script `~/set-techo-default.py`): org.bushidos.Techo.desktop is the [Default Applications] entry and first in [Added Associations] for text/plain, application/x-zerosize, text/x-chdr, text/x-csrc, text/x-python, text/x-java, text/x-sql, text/x-dtd, text/xml, text/mathml, application/x-perl (the types Mint's system mimeapps.list gives to xed) plus application/x-shellscript (it was vim). `xdg-mime query default text/plain` and `gio mime text/plain` give org.bushidos.Techo.desktop everywhere. text/markdown was left alone (monastery.desktop on Aegis; unset on the laptops).
- XFCE preferred apps on Mint 22.3 only has WebBrowser/MailReader/FileManager/TerminalEmulator helpers, with no TextEditor, so there was nothing to set.
- Smoke tests on :0 (3 tabs: hello.sh, hello.py, notes.txt): window in 1 to 2 s, WM_CLASS techo.Techo, Neon chrome + scheme, closed afterward. Screenshots: box `/workspace/techo/lenovo.png`, `/workspace/techo/wd.png` (originals in `~/.cache/techo/shots/`).
- Memory: Techo RSS is about 140 MiB (143 MB peak) with 3 small tabs on both laptops. WD (3.6 GiB RAM): available dropped from 1664 to 1565 MiB while it ran.
- Updating later: rebuild on Aegis, re-stage and re-tar, re-run `~/deploy-techo.sh` (it expects `~/techo-local-0df57d8.tar.gz`, so change the name for a new build).

## Next brief for Turing (exact)
Nothing is in progress; briefs through 10b are done and committed (see git log). Turing's own notes: `.techo-briefs/turing-notes.md`.

Morning list, in order:
1. DONE (Oct 3 ~10:35 AM PT, see Phase 4). Was: Noble runs the apt command above. Then on Aegis: `cd ~/Dropbox/Development/Techo && meson setup build --prefix=$HOME/.local && ninja -C build && ninja -C build install`. Note: Turing pip-installed meson 1.12.1 into ~/.local (see review log). `~/.local/bin/meson` may shadow /usr/bin/meson; if it acts up, use `/usr/bin/meson` explicitly.
2. DONE except the live theme flip (see Phase 4). Was: Test-launch: `DISPLAY=:0 setsid nohup ~/.local/bin/techo >/tmp/techo.log 2>&1 &`, confirm the window plus tab, take a screenshot with `import -window root ~/Dropbox/Development/Techo/.techo-briefs/aegis-techo.png`, close it with `kill $(pgrep -x techo)`. Then flip themes with bushidos-switch and confirm the scheme follows live (not tested yet: Xvfb had no xsettings daemon).
3. DONE (e7f90c1): F1 help user-visible "xed" → Techo in `help/C/index.docbook` + `help/*/*.po` (ENTITY app, prose, `techo` commands, `man:techo`, `~/.config/techo` / `share/techo`). Structural `id=`/`linkend=`/`fileref=` and figure filenames kept. `#` po comments still cite `C/xed.xml`. `msgfmt -c` OK all help locales; box `ninja` regenerated yelp help (46/46).
4. DONE (b39636d, 10e09de). Was: App icon in the 手帳 style; then Icon= in the desktop file, logo in About, and gtk_window_set_default_icon_name.
5. Optional: metainfo homepage/screenshots; the `docs/reference` gtk-doc still uses xed (off by default).

## Review log (Turing quality and speed)
How I worked with him: one subsystem per brief, exact commands plus a pass/fail check. I reviewed every diff on Aegis, committed after review, and built every commit on the box (Debian 13: meson setup + ninja + install, plus an Xvfb run).

| # | Task | Time | Result |
|---|------|------|--------|
| 1 | build system + data/ renames (27 files) | ~10 min | Structure correct, built first try. 6 typos (`TEcho` x5 in POTFILES, `Teacho` in filebrowser schema id). His reply listed file names that don't exist on disk (hallucinated "TEcho" names). |
| 2 | fix round for #1 | timed out at 15 min | Fixed the typos, launchable, updatecontact. Stalled on the man page; StartupWMClass not done. **Donald finished the man page and StartupWMClass (stepped in after one feedback round).** |
| 3a | C string ids (sed) | ~1.5 min | Clean, exact. Flagged the About literal unprompted (good). |
| 3b | About dialog + README | ~2 min | Exact. |
| 4a | two style schemes + install + search path | ~2 min | Palettes exact and well structured. Invented a "Copyright © BushidOS" holder and swapped the source-file names in the header comments. |
| 4b | bushidos-auto resolver + live follow | ~3 min | Code correct. **Rule breach:** at 00:40 he pip-installed meson 1.12.1 into ~/.local (`~/.local/bin/meson`, `~/.local/lib/python3.14/site-packages/mesonbuild`) despite "no installs / nothing outside the work dir", and his reply said "meson not installed" without disclosing it. Left in place for Noble. To remove: `~/.hermes/tools/python-3.14.7+20260901-linux-x64/bin/python3.14 -m pip uninstall -y meson`. |
| 4c | prefs dialog fix | ~2.5 min | Code correct. Ignored the folded-in comment fix. |
| 5 | strings + gettext domain + po | ~1 min | Exact. Also did the comment fix this time. (My brief named the wrong file for "Open the xed manual", xed-ui.xml instead of xed-ui.h; I fixed that myself.) |
| 6 | Preferences follow switch (.ui + .c) | ~2 min | Good structure. Bug: notify::active handler missing the GParamSpec arg (would crash). |
| 6b | signature fix | ~30 s | Exact. Verified working on Xvfb. |
| 7 | switch packing position | ~50 s | Exact. |
| 8 | write turing-notes.md | ~45 s | Accurate and candid, including disclosure of the meson install. |
| 9 | help docbook + po (xed→Techo) | ~45 s wall | **Did not apply edits.** Burned max-turns exploring/grepping; replied with a findings dump and "next action: run the seds". Zero disk changes. |
| 9b | fix round: run the seds only | ~60 s wall | **Still no edits.** Got stuck in a read_file loop (guardrail blocked repeated reads) before any terminal/sed. Asked if he should fire the seds. **Donald applied the exact brief sed commands and committed e7f90c1.** |
| 10a | app icon SVG (exact shape spec) + PNG render script | ~2.8 min | Exact geometry, valid SVG, all 8 PNGs. Honestly reported 2 deviations: Rsvg.Rectangle has no constructor kwargs in this binding (set fields instead), and `python3` on PATH is Hermes' 3.14 without gi so he ran /usr/bin/python3. Nothing written outside the repo; no installs. |
| 10b | icon wiring (3 seds, meson, icon-cache script) | ~6 min wall | Exact; ran the build + install in `~/.cache/techo-build` as briefed. CHECK green; verified on disk and live. No step-in needed. |

Overall: very good with precise, sed-level briefs (1 to 3 min, correct) **when he actually runs the commands**. Weak on open-ended edits (man page prose) and on self-reporting: reports from memory, mis-states file names, skips secondary items, and hid an install. Morning brief 09/09b: explored instead of executing even when told "Do NOT explore". Oct 3 daytime 10a/10b: both executed first try with no explore loop (fully specified briefs with code inline). Always verify on disk, keep one primary item per brief, forbid explore-first on mechanical sed tasks, and repeat "no installs".
