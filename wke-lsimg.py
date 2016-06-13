#!/usr/bin/python3

import sys
from docker import Client

WKE_PREFIX = "wke"

cli = Client()
images = cli.images()

for i in images:
    tag = i['RepoTags']
    if tag[0].startswith(WKE_PREFIX + "/"):
        print(tag[0][4:-7])

