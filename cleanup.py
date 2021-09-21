#!/usr/bin/env python3

import constants
from ghapi.all import GhApi
import envs
from pathlib import Path
from utils import maybe_delete_ssh_public_key


def main():
    gh_client = GhApi(token=envs.GITHUB_TOKEN)
    # Delete SSH key
    maybe_delete_ssh_public_key(gh_client, constants.SSH_KEY_ID_FILE_NAME)


if __name__ == '__main__':
    main()
