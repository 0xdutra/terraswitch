import platform
import os

from terraswitch.crawler import Crawler
from terraswitch.install import Install
from terraswitch.config import Config

class Download():
    def __init__(self, url):
        self._url = url

    def _get_architecture(self):
        arch = platform.machine()

        if arch == 'x86_64':
            arch = 'amd64'
        elif arch == 'i386':
            arch = '386'

        return arch

    def _get_os(self):
        os = platform.system().lower()
        return os

    def download(self, version):
        config = Config(version)
        version_path = config.create_version_path()

        arch = self._get_architecture()
        os = self._get_os()

        zip_file = f"terraform_{version}_{os}_{arch}.zip"
        url = f"{self._url}/{version}/{zip_file}"

        install = Install(zip_file)

        if version_path is not False:
            print(f"[+] - Downloading version {version} of Terraform")

            crawler = Crawler(url)
            download = crawler.request()

            with open(zip_file, 'wb') as file:
                file.write(download.content)

        install.install_binary()
        print(f"[+] - Terraform in version {version} has been successfully installed.")
