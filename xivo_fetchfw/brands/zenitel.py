__version__ = "$Revision$ $Date$"
__license__ = """
    Copyright (C) 2010  Proformatique <technique@proformatique.com>

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# XXX (2010-07-05) This is work in progress. The IP station firmware is
# not publicly available and I'm in contact with the guys at Zenitel to
# see if it will become public or not.
 
import os.path
from xivo_fetchfw import fetchfw


def zenitel_install(firmware):
    fw_dst_dir = os.path.join(fetchfw.TFTP_PATH)
    fetchfw.makedirs(fw_dst_dir)
    fetchfw.zip_extract_files(firmware.remote_files[0], (), fw_dst_dir)


fetchfw.register_install_fn('Zenitel', None, zenitel_install)
