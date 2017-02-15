#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
#                     Installer for Rsync Thread
#
# Version: 0.1                                      Date: 15 February 2017
#
# Revision History
#  15 February 2017     v0.1
#       - initial implementation
#

import weewx

from distutils.version import StrictVersion
from setup import ExtensionInstaller

REQUIRED_VERSION = "3.2.0"
RSYNC_THREAD_VERSION = "0.1"

def loader():
    return ThreadedRsyncInstaller()

class ThreadedRsyncInstaller(ExtensionInstaller):
    def __init__(self):
        if StrictVersion(weewx.__version__) < StrictVersion(REQUIRED_VERSION):
            msg = "%s requires weeWX %s or greater, found %s" % ('RsyncThread ' + RSYNC_THREAD_VERSION, 
                                                                 REQUIRED_VERSION, 
                                                                 weewx.__version__)
            raise weewx.UnsupportedFeature(msg)
        super(ThreadedRsyncInstaller, self).__init__(
            version=RSYNC_THREAD_VERSION,
            name='RsyncThread',
            description='weeWX support for anytime transfer of files using rsync.',
            author="Gary Roderick",
            author_email="gjroderick@gmail.com",
            archive_services=['user.rsyncthread.Rsync'],
            config={
                'RsyncThread': {
                    'enable': 'True',
                    'remote_path': 'replace_me',
                    'server': 'replace_me',
                    'user': 'replace_me',
                    'port': '',
                    'delete': '',
                    'ssh_timeout': '2',
                    'rsync_timeout': '2'
                }
            },
            files=[('bin/user', ['bin/user/rsyncthread.py'])]
        )
