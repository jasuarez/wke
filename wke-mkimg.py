#!/usr/bin/python3

import sys
from docker import Client

WKE_URL = "https://raw.githubusercontent.com/jasuarez/dockerfiles/wke/wke"
WKE_PROFILE = sys.argv[1]
WKE_PREFIX = "wke"

cli = Client()

fullurl = WKE_URL + "/" + WKE_PROFILE + "/Dockerfile"
fulltag = WKE_PREFIX + "/" + WKE_PROFILE

result = cli.build(path=fullurl, tag=fulltag, pull=True, decode=True)
for s in result:
    for k,v in s.items():
        print(v)

