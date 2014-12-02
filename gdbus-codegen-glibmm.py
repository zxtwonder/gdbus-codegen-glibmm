#!/usr/bin/python

# GDBus - GLib D-Bus Library
#
# Copyright (C) 2008-2011 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General
# Public License along with this library; if not, see <http://www.gnu.org/licenses/>.
#
# Author: David Zeuthen <davidz@redhat.com>


import os
import sys

srcdir = os.getenv('UNINSTALLED_GLIB_SRCDIR', None)

if srcdir is not None:
    path = os.path.join(srcdir, 'gio', 'gdbus-2.0')
elif os.name == 'nt':
    # Makes gdbus-codegen 'relocatable' at runtime on Windows.
    path = os.path.join(os.path.dirname(__file__), '..', 'share', 'glib-2.0')
else:
    path = os.path.join('/usr/share', 'glib-2.0')

sys.path.insert(0, os.path.abspath(path))
sys.path.insert(0, ".")
from codegen import codegen_main

sys.exit(codegen_main.codegen_main())