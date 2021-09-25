#!/usr/bin/env python3

import constants
import envs
from gh_auth import initialize_gh_client
from utils import maybe_delete_ssh_public_key


def main():
    gh_client = initialize_gh_client(envs.GITHUB_TOKEN,
                                     constants.GITHUB_CLIENT_ID,
                                     constants.GITHUB_TOKEN_FILE_NAME,
                                     constants.GITHUB_SCOPE,
                                     constants.GITHUB_AUTH_N_POLLS)
    # Delete SSH key
    maybe_delete_ssh_public_key(gh_client, constants.SSH_KEY_ID_FILE_NAME)


if __name__ == '__main__':
    main()
