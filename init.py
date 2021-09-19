#!/usr/bin/env python3

from ghapi.all import GhApi
import envs
import constants
from pathlib import Path
from utils import shell_run, add_user, \
    move_file_with_replacements, generate_ssh_key_pair, \
    upload_ssh_public_key, write_text







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
    gh_client = GhApi(token=envs.GITHUB_TOKEN)
    generate_ssh_key_pair(constants.SSH_KEY_TYPE, envs.EMAIL,
                          constants.SSH_KEY_FILE_NAME)
    ssh_key_id = upload_ssh_public_key(gh_client, constants.SSH_KEY_NAME,
                                       constants.SSH_KEY_FILE_NAME)
    write_text(constants.SSH_KEY_ID_FILE_NAME, ssh_key_id)
    #  git_clone(constants.CONFIGS_URL, constants.CONFIGS_DIR, constants.SSH_KEY_FILE_NAME)

    _move_configs()

    # shell_run("vim -E -c \"PlugInstall\" -c \"qall\"")

    add_user(envs.DOCKER_USER, envs.DOCKER_PASSWORD)




if __name__ == '__main__':
    main()
