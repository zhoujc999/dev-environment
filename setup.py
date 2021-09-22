#!/usr/bin/env python3

from utils import shell_run, http_install, http_download
from tempfile import NamedTemporaryFile
import constants
import envs


def main():
    for http_package in constants.HTTP_PACKAGES:
        http_install(http_package)
    for download_file in constants.DOWNLOAD_FILES:
        http_download(download_file)


if __name__ == '__main__':
    main()
