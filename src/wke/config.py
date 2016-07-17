from xdg.BaseDirectory import xdg_config_dirs
import os.path
import ConfigParser

class Config(object):
    def __init__(self):
        self._config = ConfigParser.SafeConfigParser()
        self._config.optionxform = str
        self._config.read([os.path.join(c, "wke", "defaults.conf")
                           for c in xdg_config_dirs])
        if self._config.has_option('global', 'wke'):
            self._prefix = self._config.get('global', 'wke')
        else:
            self._prefix = "wke"
        if self._config.has_option('global', 'privileged'):
            self._privileged = self._config.getboolean('global', 'privileged')
        else:
            self._privileged = False

    def get_canonical_image(self, image):
        return self._prefix + "/" + image

    def get_canonical_env(self, env):
        return self._prefix + "-" + env

    def get_source_image(self, image):
        images = self._config.get('global', 'images')
        return images + "/" + image + "/Dockerfile"

    def get_mount_points(self):
        binds = []
        for b in self._config.options('binds'):
            binds.append(b + ":" + self._config.get('binds', b))
        return binds

    def get_env_vars(self):
        envvars = []
        for e in self._config.options('envvars'):
            envvars.append(e + "=" + self._config.get('envvars', e))
        return envvars
    def is_privileged(self):
        return self._privileged
