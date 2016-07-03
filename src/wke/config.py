from xdg.BaseDirectory import xdg_config_dirs
import os.path
import ConfigParser

_WKE_URL = "https://raw.githubusercontent.com/jasuarez/dockerfiles/wke/wke"

class Config(object):
    def __init__(self):
        self._WKE_BINDS = ["/home/jasuarez/Container/:/home/jasuarez/external:rw"]
        self._config = ConfigParser.SafeConfigParser({"prefix": "wke"})
        self._config.read([os.path.join(c, "wke", "defaults.conf")
                           for c in xdg_config_dirs])

    def get_canonical_image(self, image):
        return self._config.get('globals', 'prefix') + "/" + image

    def get_canonical_env(self, env):
        return self._config.get('globals', 'prefix') + "-" + env

    def get_source_image(self, image):
        images = self._config.get('globals', 'images')
        return images + "/" + image + "/Dockerfile"

    def get_mount_points(self):
        return self._WKE_BINDS

