from collections import namedtuple
import envs

HTTPPackage = namedtuple("HTTPPackage", "url commands")
DownloadFile = namedtuple("DownloadFile", "url file_name")
MoveWithReplacements = namedtuple("MoveWithReplacements", "source destination replacements")

HOME_DIR = f"/home/{envs.DOCKER_USER}"
DOCKER_FILES_DIR = f"{HOME_DIR}/.docker_files"
CONFIGS_DIR = f"{DOCKER_FILES_DIR}/configs"

# HTTP Packages
pip = HTTPPackage("https://bootstrap.pypa.io/get-pip.py",
                  ["python3 {file_name}"])
n = HTTPPackage("https://raw.githubusercontent.com/tj/n/master/bin/n",
                ["bash {file_name} lts"])
starship = HTTPPackage("https://starship.rs/install.sh",
                       ["sh {file_name} --yes"])

HTTP_PACKAGES = [
    pip,
    n,
    starship
]

# Download Files
vim_plug = DownloadFile("https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
                        f"{HOME_DIR}/.vim/autoload/plug.vim")

DOWNLOAD_FILES = [vim_plug]

git_config = MoveWithReplacements(f"{CONFIGS_DIR}/.gitconfig",
                                  f"{HOME_DIR}/.gitconfig",
                                  {"email": envs.EMAIL, "name": envs.NAME})

vimrc = MoveWithReplacements(f"{CONFIGS_DIR}/.vimrc",
                             f"{HOME_DIR}/.vimrc",
                             None)

fish_config = MoveWithReplacements(f"{CONFIGS_DIR}/config.fish",
                                   f"{HOME_DIR}/.config/fish/config.fish",
                                   None)

starship_config = MoveWithReplacements(f"{CONFIGS_DIR}/starship.toml",
                                       f"{HOME_DIR}/.config/starship.toml",
                                       None)


MOVE_WITH_REPLACEMENTS = [
    git_config,
    vimrc,
    fish_config,
    starship_config
]


SSH_KEY_FILE_NAME = f"{HOME_DIR}/.ssh/id_ed25519"
SSH_KEY_ID_FILE_NAME = f"{HOME_DIR}/.docker_files/ssh_key_id"
SSH_KEY_TYPE = "ed25519"
SSH_KEY_NAME = "Docker"
