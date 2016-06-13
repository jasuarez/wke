#!/usr/bin/python3

import sys
from docker import Client

WKE_PREFIX = "wke"

cli = Client()
containers = cli.containers(all=True, filters={"name": WKE_PREFIX + "-"})

for c in containers:
    names = c['Names']
    print(names[0][5:])

