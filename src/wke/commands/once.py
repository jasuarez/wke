import calendar
import time
from subprocess import call

class Command(object):
    def __init__(self, docker_client, config):
        self.docker_client = docker_client
        self.config = config

    def expected_params(self):
        return 1

    def usage(self):
        return "<workenv> | <image>"

    def run(self, profile):
        timestamp = str(calendar.timegm(time.gmtime()))
        cworkenv = self.config.get_canonical_env(profile)
        filters = {"name": cworkenv}
        containers = self.docker_client.containers(all = True,
                                                   filters = filters)
        if len(containers) > 0:
            self.run_once_workenv(cworkenv, containers[0], timestamp)
        else:
            self.run_once_image(profile, timestamp)

    def run_once_workenv(self, cworkenv, container, timestamp):
        image = container['Image']
        prefix = self.config.get_canonical_image("")
        hostname = image[len(prefix):] + "/" + timestamp
        clone = self.docker_client.commit(container = cworkenv,
                                          repository = image,
                                          tag = timestamp)
        call(["docker", "run", "--privileged", "-t", "-i", "--rm",
              "-h", hostname,
              "-v", self.config.get_mount_points()[0],
              clone['Id']])
        self.docker_client.remove_image(clone['Id'])

    def run_once_image(self, image, timestamp):
        cimage = self.config.get_canonical_image(image)
        images = self.docker_client.images()
        for i in images:
            tag = i['RepoTags']
            if tag[0] == cimage + ":latest":
                hostname = image + "/" + timestamp
                call(["docker", "run", "--privileged", "-t", "-i", "--rm",
                      "-h", hostname,
                      "-v", self.config.get_mount_points()[0],
                      i['Id']])

