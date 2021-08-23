import envs

HOME_DIR = f"/home/{envs.DOCKER_USER}"

N_FILE_NAME = f"{HOME_DIR}/bin/n"
STARSHIP_FILE_NAME = f"{HOME_DIR}/bin/starship"
VIM_PLUG_FILE_NAME = f"{HOME_DIR}/.vim/autoload/plug.vim"

N_URL = "https://raw.githubusercontent.com/tj/n/master/bin/n"
STARSHIP_URL = "https://starship.rs/install.sh"
VIM_PLUG_URL = "https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim"


SSH_KEY_FILE_NAME = f"{HOME_DIR}/.ssh/id_ed25519"
SSH_KEY_TYPE = "ed25519"
SSH_KEY_NAME = "Docker"

CONFIGS_DIR = f"{HOME_DIR}/.docker_files/configs"
CONFIGS_URL = f"git@github.com:{envs.DOCKER_USER}/configs.git"


GIT_CONFIG_FILE_NAME = f"{HOME_DIR}/.gitconfig"
VIMRC_FILE_NAME = f"{HOME_DIR}/.vimrc"
FISH_CONFIG_FILE_NAME = f"{HOME_DIR}/.config/fish/config.fish"
STARSHIP_CONFIG_FILE_NAME = f"{HOME_DIR}/.config/starship.toml"

GIT_CONFIG_REPLACEMENTS = {
    "email": envs.EMAIL,
    "name": envs.NAME
}
