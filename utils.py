from subprocess import run, PIPE, STDOUT
from os import environ
from shlex import split
from urllib.request import urlopen, Request
from pathlib import Path
from crypt import crypt
from tempfile import NamedTemporaryFile


def shell_run(shell_command, silent=False):
    if not silent:
        print(shell_command)
    shell_result = run(split(shell_command), text=True, stderr=STDOUT, stdout=PIPE)
    if shell_result.returncode != 0:
        raise RuntimeError(shell_result.stdout)
    else:
        if not silent:
            print(shell_result.stdout)


def http_download(download_file_info):
    download_file(download_file_info.url, download_file_info.file_name)

def download_file(url, file_name):
    request = Request(url, headers={"User-Agent": "curl/7.64.1"})
    with urlopen(request) as remote_file:
        write_text(file_name, remote_file.read().decode("utf-8"))


def http_install(http_package_info):
    with NamedTemporaryFile() as f:
        download_file(http_package_info.url, f.name)
        for command in http_package_info.commands:
            shell_run(command.format(file_name=f.name))


def make_parent_dirs(file_name):
    file = Path(file_name)
    file.parent.mkdir(exist_ok=True, parents=True)


def write_text(file_name, string):
    make_parent_dirs(file_name)
    Path(file_name).write_text(string)


def move_file_with_replacements(source, destination, replacements=None):
    """
    Move file and replace placeholders with entries in replacements
    dictionary.
    """
    with open(source) as source_file:
        source_string = source_file.read()
        if replacements:
            source_string = source_string.format(**replacements)
        write_text(destination, source_string)


def add_user(username, password):
    print(f"Adding user: {username}")
    shell_run(f"useradd -p {crypt(password)} {username}", silent=True)
    shell_run(f"usermod -a -G sudo {username}", silent=True)


def upload_ssh_public_key(gh_client, ssh_key_name, ssh_key_file_name):
    print("Uploading SSH key to GitHub...")
    with open(f"{ssh_key_file_name}.pub", "r") as ssh_key_file:
        ssh_key = ssh_key_file.read()
    key_info = gh_client.users.create_public_ssh_key_for_authenticated(
        ssh_key_name, ssh_key)
    return f"{key_info.id}"

def delete_ssh_public_key(gh_client, key_id):
    print("Deleting SSH key from GitHub...")
    gh_client.users.delete_public_ssh_key_for_authenticated(key_id)

def generate_ssh_key_pair(ssh_key_type, email, ssh_key_file_name):
    print("Generating SSH key...")
    make_parent_dirs(ssh_key_file_name)
    shell_run(f"ssh-keygen -t {ssh_key_type} -C \"{email}\" "
              f"-P \"\" -f \"{ssh_key_file_name}\"")


def git_clone(repo_url, repo_dir, ssh_key_file_name):
    shell_run(f"git clone {repo_url} {repo_dir} --config core.sshCommand=\"ssh -i {ssh_key_file_name}\"")


class TemporaryEnv:
    def __init__(self):
        self.name = None

    def __enter__(self, name, value):
        self.name = name
        environ[self.name] = value

    def __exit__(self):
        del environ[self.name]

