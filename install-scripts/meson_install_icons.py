#!/usr/bin/python3

import os
import subprocess

icondir = os.path.join(os.environ['MESON_INSTALL_PREFIX'], 'share', 'icons', 'hicolor')

if not os.environ.get('DESTDIR'):
    print('Updating icon cache...')
    subprocess.call(['gtk-update-icon-cache', '-q', '-t', '-f', icondir])
