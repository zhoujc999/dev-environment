#!/usr/bin/env python3

import envs
import constants
from gh_auth import initialize_gh_client
from pathlib import Path
from utils import shell_run
from utils import move_file_with_replacements
from utils import maybe_add_user
from utils import maybe_generate_ssh_key_pair
from utils import maybe_upload_ssh_public_key


def main():
    gh_client = initialize_gh_client(envs.GITHUB_TOKEN,
                                     constants.GITHUB_CLIENT_ID,
                                     constants.GITHUB_TOKEN_FILE_NAME,
                                     constants.GITHUB_SCOPE,
                                     constants.GITHUB_AUTH_N_POLLS)
    maybe_generate_ssh_key_pair(constants.SSH_KEY_TYPE, envs.EMAIL,
                          constants.SSH_KEY_FILE_NAME)
    ssh_key_id = maybe_upload_ssh_public_key(gh_client, constants.SSH_KEY_NAME,
                                             constants.SSH_KEY_FILE_NAME,
                                             constants.SSH_KEY_ID_FILE_NAME)

    for move in constants.MOVE_WITH_REPLACEMENTS:
        move_file_with_replacements(move.source, move.destination,
                                    move.replacements)

    shell_run("vim -c 'PlugInstall' -c 'qall!'")

    maybe_add_user(envs.DOCKER_USER, envs.DOCKER_PASSWORD)


if __name__ == '__main__':
    main()
