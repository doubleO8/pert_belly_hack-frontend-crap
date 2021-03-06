#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import __version__

#: meta data for opkg
PACKAGE_META = {
    "package": "pert-belly-hack-frontend-crap",
    "upstream_version": __version__,
    "epoch": 2,
    "target_root_path": "OpenWebif",
    "description": "frontend component providing the outdated Browser UI",
    "depends": 'python-json, python-cheetah, python-unixadmin, python-misc, python-twisted-web, python-pprint, python-compression, python-ipaddress, pert-belly-hack-backend',
    "conflicts": "enigma2-plugin-extensions-openwebif",
}

TAG_PATH_REL = 'public/tag_frontend-crap.json'
