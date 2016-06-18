#!/usr/bin/python3

import sys
import time
import calendar
from subprocess import call
from docker import Client

WKE_NAME = sys.argv[1]
WKE_PREFIX = "wke"
WKE_BINDS = ["/home/jasuarez/Container/:/home/jasuarez/external:rw"]

fullenv = WKE_PREFIX + "-" + WKE_NAME
fullimg = WKE_PREFIX + "/" + WKE_NAME

timestamp = str(calendar.timegm(time.gmtime()))
cli = Client()
containers = cli.containers(all=True, filters={"name": fullenv})

if len(containers) > 0:
    image = containers[0]['Image']
    hostname = image[len(WKE_PREFIX):] + "/" + timestamp
    clone = cli.commit(container=fullenv, repository=image, tag=timestamp);
    call(["docker", "run", "--privileged", "-t", "-i", "--rm", "-h", hostname, "-v", WKE_BINDS[0], clone['Id']])
    cli.remove_image(clone['Id'])
else:
    images = cli.images()
    for i in images:
        tag = i['RepoTags']
        if tag[0] == fullimg + ":latest":
            hostname = WKE_NAME + "/" + timestamp
            call(["docker", "run", "--privileged", "-t", "-i", "--rm", "-h", hostname, "-v", WKE_BINDS[0], i['Id']])
