#!/usr/bin/env python3

from utils import shell_run, download_file
import constants
import envs


def _install_node_and_npm():
    download_file(constants.N_URL, constants.N_FILE_NAME)
    shell_run(f"bash {constants.N_FILE_NAME} lts")

def _install_starship():
    download_file(constants.STARSHIP_URL, constants.STARSHIP_FILE_NAME)
    shell_run(f"sh {constants.STARSHIP_FILE_NAME} --yes")

def _download_vim_plug():
    download_file(constants.VIM_PLUG_URL, constants.VIM_PLUG_FILE_NAME)



def main():
    _install_node_and_npm()
    _install_starship()
    _download_vim_plug()




if __name__ == '__main__':
    main()
