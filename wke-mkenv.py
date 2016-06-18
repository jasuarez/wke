#!/usr/bin/python3

import sys
from docker import Client

WKE_IMAGE = sys.argv[2]
WKE_ENV = sys.argv[1]
WKE_PREFIX = "wke"
WKE_BINDS = ["/home/jasuarez/Container/:/home/jasuarez/external:rw"]

cli = Client()

fullimg = WKE_PREFIX + "/" + WKE_IMAGE
fullenv = WKE_PREFIX + "-" + WKE_ENV

envvars = {"DOCKER_NAME": WKE_ENV}

result = cli.create_container(image = fullimg,
                              hostname = WKE_IMAGE,
                              host_config = cli.create_host_config(binds = WKE_BINDS,
                                                                   privileged = True),
                              stdin_open = True,
                              tty = True,
                              name = fullenv,
                              environment = envvars)
for s in result:
    print(s)

