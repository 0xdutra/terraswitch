import os
from os import path

class Config:
    def __init__(self, version):
        self._version = version

    def _check_version_exist(self, version_path):
        if(path.exists(version_path)):
            return True
        return False

    def create_version_path(self):
        user_home = os.getenv('HOME')
        terraswitch_home = f"{user_home}/.terraswitch"
        version_home = f"{terraswitch_home}/{self._version}"

        if self._check_version_exist(version_home) is False:
            os.makedirs(version_home)
            os.chdir(version_home)
            return True

        os.chdir(version_home)
        return False
