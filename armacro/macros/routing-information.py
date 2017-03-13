# -*- coding: utf-8 -*-
# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

"""
Collects routing information

Usage:

    bash armacro system-information
"""

from __future__ import print_function

from armacro.utils import cli
from pprint import pprint

"""
show ip bgp | json
{
    "vrfs": {
        "default": {
            "routerId": "10.0.0.1",
            "vrf": "default",
            "bgpRouteEntries": {
                "5.1.3.0/24": {
                    "bgpAdvertisedPeerGroups": {},
                    "maskLength": 24,
                    "bgpRoutePaths": [
                        {
                            "asPathEntry": {
                                "asPathType": null,
                                "asPath": "?"
                            },
                            "med": 0,
                            "localPreference": 100,
                            "weight": 0,
                            "reasonNotBestpath": null,
                            "nextHop": "169.254.0.1",
                            "routeType": {
                                "atomicAggregator": false,
                                "suppressed": false,
                                "queued": false,
                                "valid": true,
                                "ecmpContributor": false,
                                "luRoute": false,
                                "active": true,
                                "stale": false,
                                "ecmp": false,
                                "backup": false,
                                "ecmpHead": false,
                                "ucmp": false
                            }
                        }
                    ],
                    "address": "5.1.3.0"
                },
                "5.0.1.0/24": {
                    "bgpAdvertisedPeerGroups": {},
                    "maskLength": 24,
                    "bgpRoutePaths": [
                        {
                            "asPathEntry": {
                                "asPathType": null,
                                "asPath": "?"
                            },
                            "med": 0,
                            "localPreference": 0,
                            "reasonNotBestpath": null,
                            "routeType": {
                                "atomicAggregator": false,
                                "suppressed": false,
                                "queued": false,
                                "valid": true,
                                "ecmpContributor": false,
                                "luRoute": false,
                                "active": true,
                                "stale": false,
                                "ecmp": false,
                                "backup": false,
                                "ecmpHead": false,
                                "ucmp": false
                            }
                        }
                    ],
                    "address": "5.0.1.0"
                },
                "5.1.1.0/24": {
                    "bgpAdvertisedPeerGroups": {},
                    "maskLength": 24,
                    "bgpRoutePaths": [
                        {
                            "asPathEntry": {
                                "asPathType": null,
                                "asPath": "?"
                            },
                            "med": 0,
                            "localPreference": 100,
                            "weight": 0,
                            "reasonNotBestpath": null,
                            "nextHop": "169.254.0.1",
                            "routeType": {
                                "atomicAggregator": false,
                                "suppressed": false,
                                "queued": false,
                                "valid": true,
                                "ecmpContributor": false,
                                "luRoute": false,
                                "active": true,
                                "stale": false,
                                "ecmp": false,
                                "backup": false,
                                "ecmpHead": false,
                                "ucmp": false
                            }
                        }
                    ],
                    "address": "5.1.1.0"
                }
                ...
            },
            "asn": 65535
        }
    }
}

veos-sdf-01#show ip route | json
{
    "vrfs": {
        "default": {
            "routes": {
                "172.16.128.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": true,
                    "routeAction": "forward",
                    "vias": [
                        {
                            "interface": "Management1"
                        }
                    ],
                    "hardwareProgrammed": true,
                    "routeType": "connected"
                },
                "5.0.1.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": true,
                    "routeAction": "drop",
                    "vias": [],
                    "hardwareProgrammed": true,
                    "routeType": "static"
                },
                "5.1.1.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": false,
                    "preference": 200,
                    "routeAction": "forward",
                    "vias": [
                        {
                            "interface": "Port-Channel1",
                            "nexthopAddr": "169.254.0.1"
                        }
                    ],
                    "metric": 0,
                    "hardwareProgrammed": true,
                    "routeType": "iBGP"
                },
                "5.1.2.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": false,
                    "preference": 200,
                    "routeAction": "forward",
                    "vias": [
                        {
                            "interface": "Port-Channel1",
                            "nexthopAddr": "169.254.0.1"
                        }
                    ],
                    "metric": 0,
                    "hardwareProgrammed": true,
                    "routeType": "iBGP"
                },
                "192.168.101.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": true,
                    "routeAction": "forward",
                    "vias": [
                        {
                            "interface": "Vlan101"
                        }
                    ],
                    "hardwareProgrammed": true,
                    "routeType": "connected"
                },
                "10.0.0.1/32": {
                    "kernelProgrammed": true,
                    "directlyConnected": true,
                    "routeAction": "forward",
                    "vias": [
                        {
                            "interface": "Loopback0"
                        }
                    ],
                    "hardwareProgrammed": true,
                    "routeType": "connected"
                },
                "5.1.4.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": false,
                    "preference": 200,
                    "routeAction": "forward",
                    "vias": [
                        {
                            "interface": "Port-Channel1",
                            "nexthopAddr": "169.254.0.1"
                        }
                    ],
                    "metric": 0,
                    "hardwareProgrammed": true,
                    "routeType": "iBGP"
                },
                "5.0.0.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": true,
                    "routeAction": "drop",
                    "vias": [],
                    "hardwareProgrammed": true,
                    "routeType": "static"
                },
                "5.0.3.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": true,
                    "routeAction": "drop",
                    "vias": [],
                    "hardwareProgrammed": true,
                    "routeType": "static"
                },
                "5.1.3.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": false,
                    "preference": 200,
                    "routeAction": "forward",
                    "vias": [
                        {
                            "interface": "Port-Channel1",
                            "nexthopAddr": "169.254.0.1"
                        }
                    ],
                    "metric": 0,
                    "hardwareProgrammed": true,
                    "routeType": "iBGP"
                },
                "5.1.0.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": false,
                    "preference": 200,
                    "routeAction": "forward",
                    "vias": [
                        {
                            "interface": "Port-Channel1",
                            "nexthopAddr": "169.254.0.1"
                        }
                    ],
                    "metric": 0,
                    "hardwareProgrammed": true,
                    "routeType": "iBGP"
                },
                "5.0.4.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": true,
                    "routeAction": "drop",
                    "vias": [],
                    "hardwareProgrammed": true,
                    "routeType": "static"
                },
                "5.0.2.0/24": {
                    "kernelProgrammed": true,
                    "directlyConnected": true,
                    "routeAction": "drop",
                    "vias": [],
                    "hardwareProgrammed": true,
                    "routeType": "static"
                },
                "169.254.0.0/31": {
                    "kernelProgrammed": true,
                    "directlyConnected": true,
                    "routeAction": "forward",
                    "vias": [
                        {
                            "interface": "Port-Channel1"
                        }
                    ],
                    "hardwareProgrammed": true,
                    "routeType": "connected"
                }
            },
            "allRoutesProgrammedKernel": true,
            "routingDisabled": true,
            "allRoutesProgrammedHardware": true,
            "defaultRouteState": "notSet"
        }
    }
}

"""


def main():
    commands = ["show ip bgp", "show ip route"]

    bgp_routes, all_routes = cli(commands, "json")

    all_routes = all_routes["vrfs"]["default"]["routes"]
    bgp_routes = bgp_routes["vrfs"]["default"]["bgpRouteEntries"]

    print("PREFIX\t\tTYPE\tHARDWARE")

    for prefix, details in all_routes.iteritems():
        print("{}\t{}\t{}".format(prefix, details["routeType"], details["hardwareProgrammed"]))
