# -*- coding: utf-8 -*-
# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

"""
Collects system information

Usage:

    bash armacro system-information
"""

from __future__ import print_function

from armacro.utils import cli
from pprint import pprint

def main():
    commands = ["show version", "show inventory", "show hostname"]

    version, inventory, hostname = cli(commands, "json")

    print("""
System Summary:

Hostname (FQDN):  {} ({})
Model:            {}
Software Version: {}
Description:      {}
Data Ports:       {}
""".format(hostname["hostname"], hostname["fqdn"],
           inventory["systemInformation"]["name"], version["version"],
           inventory["systemInformation"]["description"],
           inventory["switchedPortCount"]))
