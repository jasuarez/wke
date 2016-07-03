SUMMARY = "create a new working environment"

class Command(object):
    def __init__(self, docker_client, config):
        self.docker_client = docker_client
        self.config = config

    def expected_params(self):
        return 2

    def usage(self):
        return "<workenv> <image>"

    def run(self, workenv, image):
        envvars = {"DOCKER_NAME": workenv}
        cworkenv = self.config.get_canonical_env(workenv)
        cimage = self.config.get_canonical_image(image)
        binds = self.config.get_mount_points()
        host_config = self.docker_client.create_host_config(privileged = True,
                                                            binds = binds)
        result = self.docker_client.create_container(image = cimage,
                                                     hostname = image,
                                                     host_config = host_config,
                                                     stdin_open = True,
                                                     tty = True,
                                                     name = cworkenv,
                                                     environment = envvars)
        for s in result:
            print(s)
