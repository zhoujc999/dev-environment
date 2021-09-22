#!/usr/bin/env python3

from ghapi.all import GhApi
import envs
import constants
from pathlib import Path
from utils import shell_run
from utils import move_file_with_replacements
from utils import maybe_add_user
from utils import maybe_generate_ssh_key_pair
from utils import maybe_upload_ssh_public_key


def main():
    gh_client = GhApi(token=envs.GITHUB_TOKEN)
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
