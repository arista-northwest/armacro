# -*- coding: utf-8 -*-
# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

from __future__ import print_function

import jsonrpclib
import sys
import socket
import sys

NO_EAPI_MESSAGE = """Error: Cannot issue eAPI commands.

Please verify that EAPI is enabled:

    management api http-commands
       protocol unix-socket
       no shutdown
"""

def cli(commands, encoding="text"):
    eapi = jsonrpclib.Server("unix:/var/run/command-api.sock")

    try:
        results = eapi.runCmds(1, ["enable"] + commands, encoding)
    except jsonrpclib.jsonrpc.ProtocolError as exc:
        print("Error: [{}] {}".format(exc.message[0], exc.message[1]))
        sys.exit(-1)
    except socket.error:
        print(NO_EAPI_MESSAGE)
        sys.exit(-1)

    if encoding == "text":
        results = [res["output"] for res in results]

    return results[1:]
