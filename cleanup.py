#!/usr/bin/env python3

import constants
from ghapi.all import GhApi
import envs
from pathlib import Path
from utils import delete_ssh_public_key








def main():
    gh_client = GhApi(token=envs.GITHUB_TOKEN)
    # Delete SSH key
    with open(constants.SSH_KEY_ID_FILE_NAME) as ssh_key_id_file:
        ssh_key_id = ssh_key_id_file.read()
        delete_ssh_public_key(gh_client, ssh_key_id)




if __name__ == '__main__':
    main()
