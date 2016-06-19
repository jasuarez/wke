from subprocess import call

class Command(object):
    def __init__(self, docker_client, config):
        self.docker_client = docker_client
        self.config = config

    def expected_params(self):
        return 1

    def usage(self):
        return "<workenv>"

    def run(self, workenv):
        cworkenv = self.config.get_canonical_env(workenv)
        call(["docker", "start", "-a", "-i", cworkenv])

