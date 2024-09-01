#!/usr/bin/env python3

import envs
import constants
from utils import shell_run
from utils import move_file_with_replacements
from utils import maybe_add_user
from utils import maybe_generate_ssh_key_pair
from utils import maybe_upload_ssh_public_key


def main():
    maybe_generate_ssh_key_pair(constants.SSH_KEY_TYPE, envs.EMAIL,
                          constants.SSH_KEY_FILE_NAME)

    for move in constants.MOVE_WITH_REPLACEMENTS:
        move_file_with_replacements(move.source, move.destination,
                                    move.replacements)

    maybe_add_user(envs.DOCKER_USER, envs.DOCKER_PASSWORD)


if __name__ == '__main__':
    main()
