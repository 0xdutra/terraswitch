import os
import sys
import errno
import stat

from os import path
from zipfile import ZipFile


class Install:
    def __init__(self, path):
        self.path = path

    def _extract_file(self):
        with ZipFile(self.path, 'r') as zipFile:
            zipFile.extractall()

    def _search_bin_path(self):
        return os.getenv("PATH").split(':')

    def _set_exec_permission(self, binary):
        try:
            st = os.stat(binary)
            os.chmod(binary, st.st_mode | stat.S_IEXEC)
        except Exception as e:
            print(e)
            sys.exit(1)

    def _get_current_user(self):
        return os.getuid()

    def _get_current_directory(self):
        return os.getcwd()

    def _get_user_home(self):
        return os.getenv('HOME')

    def _create_symbolic_link(self, src, dest):
        try:
            os.symlink(src, dest)
        except Exception as e:
            print(e)
        finally:
            self._set_exec_permission(dest)

    def _remove_current_version(self, binary):
        try:
            os.remove(binary)
        except OSError as e:
            if e.errno == errno.EACCES:
                print(e)
                sys.exit(1)

    def install_binary(self):
        try:
            self._extract_file()
        except Exception as e:
            print(f"[+] - Extract failed: {e}")

        user_home = self._get_user_home()
        local_path = self._get_current_directory()
        uid = self._get_current_user()

        if uid == 0:
            terraform_bin = f"{local_path}/terraform"
            terraform_bin_local_path = "/usr/local/bin"
        else:
            terraform_bin = f"{local_path}/terraform"
            terraform_bin_local_path = f"{user_home}/.local/bin/terraform"

        if path.isfile(terraform_bin_local_path) or path.islink(
                terraform_bin_local_path):
            print("[+] - Removing current version of terraform")
            self._remove_current_version(terraform_bin_local_path)

        self._create_symbolic_link(terraform_bin, terraform_bin_local_path)

        print(f"[+] - Terraform has been successfully installed.")
