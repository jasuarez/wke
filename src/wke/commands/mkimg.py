SUMMARY = "create a new image"

class Command(object):
    def __init__(self, docker_client, config):
        self.docker_client = docker_client
        self.config = config

    def expected_params(self):
        return 1

    def usage(self):
        return "<image>"

    def run(self, image):
        url = self.config.get_source_image(image)
        cimage = self.config.get_canonical_image(image)
        result = self.docker_client.build(path = url,
                                          tag = cimage,
                                          pull = True,
                                          decode = True)
        for s in result:
            for k,v in s.items():
                print(v)
