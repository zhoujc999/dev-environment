#!/usr/bin/env python3

from github import Github
import envs
import constants
from pathlib import Path
from utils import shell_run, add_user, make_parent_dirs, \
    move_file_with_replacements, generate_ssh_key_pair, \
    upload_ssh_public_key







def _move_configs():
    move_file_with_replacements(f"{constants.CONFIGS_DIR}/.gitconfig",
                                constants.GIT_CONFIG_FILE_NAME,
                                constants.GIT_CONFIG_REPLACEMENTS)

    move_file_with_replacements(f"{constants.CONFIGS_DIR}/.vimrc",
                                constants.VIMRC_FILE_NAME)

    move_file_with_replacements(f"{constants.CONFIGS_DIR}/config.fish",
                                constants.FISH_CONFIG_FILE_NAME)

    move_file_with_replacements(f"{constants.CONFIGS_DIR}/starship.toml",
                                constants.STARSHIP_CONFIG_FILE_NAME)

def main():
    shell_run("python3 -m pip install PyGithub")

    gh_client = Github(envs.GITHUB_TOKEN)
    generate_ssh_key_pair(constants.SSH_KEY_TYPE, envs.EMAIL,
                          constants.SSH_KEY_FILE_NAME)
    #  upload_ssh_public_key(gh_client, constants.SSH_KEY_FILE_NAME,
                          #  constants.SSH_KEY_NAME)
    #  git_clone(constants.CONFIGS_URL, constants.CONFIGS_DIR, constants.SSH_KEY_FILE_NAME)

    _move_configs()

    # shell_run("vim -E -c \"PlugInstall\" -c \"qall\"")

    add_user(envs.DOCKER_USER, envs.DOCKER_PASSWORD)




if __name__ == '__main__':
    main()
