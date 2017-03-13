# -*- coding: utf-8 -*-
# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import argparse
import os
import pkgutil
import imp
import re
from utils import cli

# ====================
DEBUG = False
# search these paths for the 'armacro' directory
PATHS = ['/mnt/flash/armacro', '/persist/local/armacro']
# ====================

PATHS.insert(0,
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "macros"))

def _load_macro(name):
    modules = []

    for base_path in PATHS:
        fname = "{}/{}.py".format(base_path, name)
        if os.path.isfile(fname):
            return imp.load_source(re.sub(r"[\W\-]", "_", name), fname)


def main():
    parser = argparse.ArgumentParser(prog="armacro")
    arg = parser.add_argument

    arg("macro", help="Name of macro to run")
    args = parser.parse_args()

    macro = _load_macro(args.macro)
    macro.main()

if __name__ == '__main__':
    main()
