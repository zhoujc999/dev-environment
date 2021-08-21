#!/usr/bin/env python3

from os import getenv
from subprocess import run, PIPE, STDOUT
from github import Github
from shlex import split

GITHUB_TOKEN_ENV = "GITHUB_TOKEN"
USER_ENV = "USER"
EMAIL = "zhoujc999@gmail.com"
DEFAULT_SSH_KEY_FILE_PATH = ".ssh/id_ed25519"


def _generate_ssh_key_pair(email, user):
    shell_result = run(split(f"ssh-keygen -t ed25519 -C \"{email}\" -P \"\" -f \"{DEFAULT_SSH_KEY_FILE_PATH}\""),
        text=True, stderr=STDOUT, stdout=PIPE)
    if shell_result.returncode != 0:
        raise RuntimeError(shell_result.stdout)
    else:
        print(shell_result.stdout)

def _upload_ssh_public_key(gh_client):
    with open(DEFAULT_SSH_KEY_FILE_PATH + ".pub", "r") as ssh_key_file:
        ssh_key = ssh_key_file.read().rstrip("\n")
        print(f"SSH PUBLIC KEY: {ssh_key}")
        gh_user = gh_client.get_user().create_key("Test", ssh_key)


def main():
    gh_token = getenv(GITHUB_TOKEN_ENV)
    user = getenv(USER_ENV)
    gh_client = Github(gh_token)
    # TODO: Use getenv to get email
    _generate_ssh_key_pair(EMAIL, user)
    _upload_ssh_public_key(gh_client)


if __name__ == '__main__':
    main()
