from subprocess import run, PIPE, STDOUT
from shlex import split
from urllib.request import urlopen, Request
from pathlib import Path
from crypt import crypt


def shell_run(shell_command):
    print(shell_command)
    shell_result = run(split(shell_command), text=True, stderr=STDOUT, stdout=PIPE)
    if shell_result.returncode != 0:
        raise RuntimeError(shell_result.stdout)
    else:
        print(shell_result.stdout)


def download_file(url, file_name):
    request = Request(url, headers={"User-Agent": "curl/7.64.1"})
    with urlopen(request) as remote_file:
        write_text(file_name, remote_file.read().decode("utf-8"))


def make_parent_dirs(file_name):
    file = Path(file_name)
    file.parent.mkdir(exist_ok=True, parents=True)


def write_text(file_name, string):
    make_parent_dirs(file_name)
    Path(file_name).write_text(string)


def move_file_with_replacements(source, destination, replacements=None):
    with open(source) as source_file:
        source_string = source_file.read()
        if replacements:
            source_string = source_string.format(**replacements)
        write_text(destination, source_string)


def add_user(username, password):
    shell_run(f"useradd -p {crypt(password)} --create-home {username}")
    shell_run(f"usermod -a -G sudo {username}")
