#!/usr/bin/python3

import sys
from subprocess import call

WKE_ENV = sys.argv[1]
WKE_PREFIX = "wke"

fullenv = WKE_PREFIX + "-" + WKE_ENV

call(["docker", "start", "-a", "-i", fullenv])
