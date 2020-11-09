import time

from bs4 import BeautifulSoup
from terraswitch.crawler import Crawler


class Versions(Crawler):
    def __init__(self, url):
        super().__init__(url)
        self._versions = []

    def __getitem__(self, key):
        return self._versions[key]

    def __str__(self):
        time.sleep(5)
        return "Searching all Terraform versions...\n"

    def versions(self):
        r = self.request()
        bs = BeautifulSoup(r.text, "lxml")

        links = bs.find_all("a")

        tmp = []

        for link in links:
            version = link.text.replace("terraform_", "")
            tmp.append(version)

        # sorry :'(
        self._versions = tmp[1:-1]
