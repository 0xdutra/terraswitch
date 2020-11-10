import click

from terraswitch.versions import Versions
from terraswitch.download import Download
from terraswitch.config import Config
from terraswitch.banner import Banner
from terraswitch.install import Install


@click.command()
@click.option('--list-versions',
              '-l',
              is_flag=True,
              help="List all Terraform versions")
@click.option('--install',
              '-i',
              is_flag=True,
              help="Install Terraform version")
@click.option('--version',
              '-v',
              help="Set the version of Terraform to install")
def main(list_versions, install, version):
    banner = Banner()
    print(banner)

    url = "https://releases.hashicorp.com/terraform"

    if list_versions:
        v = Versions(url)
        print(v)

        v.versions()

        for version in v:
            print(f"[+] Terraform version: {version}")

    elif install:
        Config(version)

        download = Download(url)
        zip_file = download.download(version)

        install = Install(zip_file)
        install.install_binary()
