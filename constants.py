from collections import namedtuple
import envs

HTTPPackage = namedtuple("HTTPPackage", "url commands")
DownloadFile = namedtuple("DownloadFile", "url file_name")

HOME_DIR = f"/home/{envs.DOCKER_USER}"

# HTTP Packages
pip = HTTPPackage("https://bootstrap.pypa.io/get-pip.py",
                  ["python3 {file_name}"])
n = HTTPPackage("https://raw.githubusercontent.com/tj/n/master/bin/n",
                ["bash {file_name} lts"])
starship = HTTPPackage("https://starship.rs/install.sh",
                       ["sh {file_name} --yes"])

HTTP_PACKAGES = [pip,
                 n,
                 starship]

# Download Files
vim_plug = DownloadFile("https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim",
                        f"{HOME_DIR}/.vim/autoload/plug.vim")


DOWNLOAD_FILES = [vim_plug]

SSH_KEY_FILE_NAME = f"{HOME_DIR}/.ssh/id_ed25519"
SSH_KEY_ID_FILE_NAME = f"{HOME_DIR}/.docker_files/ssh_key_id"
SSH_KEY_TYPE = "ed25519"
SSH_KEY_NAME = "Docker"

DOCKER_FILES_DIR = f"{HOME_DIR}/.docker_files"
CONFIGS_DIR = f"{HOME_DIR}/.docker_files/configs"


GIT_CONFIG_FILE_NAME = f"{HOME_DIR}/.gitconfig"
VIMRC_FILE_NAME = f"{HOME_DIR}/.vimrc"
FISH_CONFIG_FILE_NAME = f"{HOME_DIR}/.config/fish/config.fish"
STARSHIP_CONFIG_FILE_NAME = f"{HOME_DIR}/.config/starship.toml"

GIT_CONFIG_REPLACEMENTS = {
    "email": envs.EMAIL,
    "name": envs.NAME
}
