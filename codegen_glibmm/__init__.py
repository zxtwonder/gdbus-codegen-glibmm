# -*- Mode: Python -*-

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

# Update this as the version changes
version_info = (0, 1, 0)
version = '.'.join(str(c) for c in version_info)

builddir = os.environ.get('UNINSTALLED_GLIB_BUILDDIR')

if builddir is not None:
    __path__.append(os.path.abspath(os.path.join(builddir, 'gio', 'gdbus-2.0', 'codegen_glibmm')))
