from collections import namedtuple
import envs

HTTPPackage = namedtuple("HTTPPackage", "url commands")
DownloadFile = namedtuple("DownloadFile", "url file_name")
MoveWithReplacements = namedtuple("MoveWithReplacements", "source destination replacements")


HOME_DIR = f"/home/{envs.DOCKER_USER}"
DOCKER_FILES_DIR = f"{HOME_DIR}/.docker_files"
CONFIGS_DIR = f"{DOCKER_FILES_DIR}/configs"

# HTTP Packages
PIP = HTTPPackage("https://bootstrap.pypa.io/get-pip.py",
                  ["python3 {file_name}"])
N = HTTPPackage("https://raw.githubusercontent.com/tj/n/master/bin/n",
                ["bash {file_name} lts"])
STARSHIP = HTTPPackage("https://starship.rs/install.sh",
                       ["sh {file_name} --yes"])

HTTP_PACKAGES = [
    PIP,
    N,
    STARSHIP
]

# Download Files
VIM_PLUG = DownloadFile("https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
                        f"{HOME_DIR}/.vim/autoload/plug.vim")

DOWNLOAD_FILES = [VIM_PLUG]

GIT_CONFIG = MoveWithReplacements(f"{CONFIGS_DIR}/.gitconfig",
                                  f"{HOME_DIR}/.gitconfig",
                                  {"email": envs.EMAIL, "name": envs.NAME})

VIMRC = MoveWithReplacements(f"{CONFIGS_DIR}/.vimrc",
                             f"{HOME_DIR}/.vimrc",
                             None)

FISH_CONFIG = MoveWithReplacements(f"{CONFIGS_DIR}/config.fish",
                                   f"{HOME_DIR}/.config/fish/config.fish",
                                   None)

STARSHIP_CONFIG = MoveWithReplacements(f"{CONFIGS_DIR}/starship.toml",
                                       f"{HOME_DIR}/.config/starship.toml",
                                       None)


MOVE_WITH_REPLACEMENTS = [
    GIT_CONFIG,
    VIMRC,
    FISH_CONFIG,
    STARSHIP_CONFIG
]


SSH_KEY_FILE_NAME = f"{HOME_DIR}/.ssh/id_ed25519"
SSH_KEY_ID_FILE_NAME = f"{DOCKER_FILES_DIR}/ssh_key_id"
SSH_KEY_TYPE = "ed25519"
SSH_KEY_NAME = "Docker"

GITHUB_CLIENT_ID = "716ca4eb3c74787aa29f"
GITHUB_AUTH_N_POLLS = 9999
GITHUB_SCOPE = "admin:public_key"
GITHUB_TOKEN_FILE_NAME = f"{DOCKER_FILES_DIR}/github_token"

