import requests

class Crawler:
    def __init__(self, url):
        self.url = url

    def request(self):
        try:
            r = requests.get(url=self.url)
        except requests.exceptions.RequestException as e:
            print(f"[+] - Error: {e}")

        return r
