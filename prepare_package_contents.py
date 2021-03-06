#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
CLI tool: generate OPKG package and meta data.
"""
import pprint

import pert_belly_hack
from pert_belly_hack.packaging import AlPackino

from pert_belly_hack_frontend_crap.defaults import PACKAGE_META, TAG_PATH_REL

if __name__ == '__main__':
    print("Pert Belly Hack {:s}: {:s}".format(
        pert_belly_hack.__version__, 'PREPARE'))
    pprint.pprint(PACKAGE_META)

    AL = AlPackino(package_meta=PACKAGE_META,
                   tag_path_rel=TAG_PATH_REL)
    AL.prepare()
