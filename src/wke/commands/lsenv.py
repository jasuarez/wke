class Command(object):
    def __init__(self, docker_client, config):
        self.docker_client = docker_client
        self.config = config

    def expected_params(self):
        return 0

    def usage(self):
        return ""

    def run(self):
        prefix = self.config.get_canonical_env("")
        filters = {"name": prefix}
        containers = self.docker_client.containers(all = True,
                                                   filters = filters)
        for c in containers:
            names = c['Names']
            print(names[0][len(prefix) + 1:])

