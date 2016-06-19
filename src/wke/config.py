_WKE_PREFIX = "wke"
_WKE_URL = "https://raw.githubusercontent.com/jasuarez/dockerfiles/wke/wke"

class Config(object):
    def __init__(self):
        self._WKE_PREFIX = "wke"
        self._WKE_URL = "https://raw.githubusercontent.com/jasuarez/dockerfiles/wke/wke"
        self._WKE_BINDS = ["/home/jasuarez/Container/:/home/jasuarez/external:rw"]

        
    def get_canonical_image(self, image):
        return _WKE_PREFIX + "/" + image

    def get_canonical_env(self, env):
        return _WKE_PREFIX + "-" + env

    def get_source_image(self, image):
        return _WKE_URL + "/" + image + "/Dockerfile"

    def get_mount_points(self):
        return self._WKE_BINDS

