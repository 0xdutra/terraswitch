import click

from terraswitch.versions import Versions
from terraswitch.download import Download
from terraswitch.config import Config
from terraswitch.banner import Banner

@click.command()
@click.option('--list-versions', '-l', is_flag=True, help="List all Terraform versions")
@click.option('--install', '-i', is_flag=True, help="Install Terraform version")
@click.option('--version', '-v', help="Set the version of Terraform to install")
def main(list_versions, install, version):
    url = "https://releases.hashicorp.com/terraform"

    if list_versions:
        v = Versions(url)
        print(v)

        v.versions()

        for version in v:
            print(f"[+] Terraform version: {version}")

    elif install:
        config = Config(version)

        download = Download(url)
        download.download(version)

if __name__ == '__main__':
    banner = Banner()
    print(banner)
    main()
