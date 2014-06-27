#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from distutils.core import setup

setup(
    name='xivo-fetchfw',
    version='1.0',
    description='Library and tool for downloading and installing remote files.',
    maintainer='Proformatique',
    maintainer_email='technique@proformatique.com',
    url='http://wiki.xivo.io/',
    license='GPLv3',
    packages=['xivo_fetchfw',
              'xivo_fetchfw.cisco'],
)