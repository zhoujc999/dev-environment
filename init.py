#!/usr/bin/env python3

from github import Github
import envs
import constants
from pathlib import Path
from utils import shell_run, add_user, make_parent_dirs, move_file_with_replacements


def _generate_ssh_key_pair(ssh_key_type, email, ssh_key_file_name):
    make_parent_dirs(ssh_key_file_name)
    shell_run(f"ssh-keygen -t {ssh_key_type} -C \"{email}\" "
              f"-P \"\" -f \"{ssh_key_file_name}\"")


def _upload_ssh_public_key(gh_client, ssh_key_file_name, ssh_key_name):
    with open(f"{ssh_key_file_name}.pub", "r") as ssh_key_file:
        ssh_key = ssh_key_file.read()
    gh_user = gh_client.get_user().create_key(ssh_key_name, ssh_key)


def git_clone(repo_url, repo_dir, ssh_key_file_name):
    shell_run(f"git clone {repo_url} {repo_dir} --config core.sshCommand=\"ssh -i {ssh_key_file_name}\" -o StrictHostKeyChecking=no")

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
    gh_client = Github(envs.GITHUB_TOKEN)
    _generate_ssh_key_pair(constants.SSH_KEY_TYPE, envs.EMAIL,
                           constants.SSH_KEY_FILE_NAME)
    _upload_ssh_public_key(gh_client, constants.SSH_KEY_FILE_NAME,
                           constants.SSH_KEY_NAME)
    git_clone(constants.CONFIGS_URL, constants.CONFIGS_DIR, constants.SSH_KEY_FILE_NAME)

    _move_configs()

    add_user(envs.DOCKER_USER, envs.DOCKER_PASSWORD)




if __name__ == '__main__':
    main()
