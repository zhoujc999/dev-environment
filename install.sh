# Script for installing Linux packages
apt-get update \
&& apt-get install -y \
  sudo \
  tmux \
  git \
  curl \
  fd-find \
  ripgrep \
  vim \
  bat \
  exa \
  fzf \
  python3-pip \
  software-properties-common \
  locales \
&& locale-gen en_US.UTF-8 \
&& update-locale LANG=en_US.UTF-8 \
&& apt-add-repository ppa:fish-shell/release-3 \
&& apt-get update \
&& apt-get install -y fish \
&& curl -L https://raw.githubusercontent.com/tj/n/master/bin/n -o n \
&& bash n lts \
&& rm -rf /var/lib/apt/lists/* \
&& python3 -m pip install PyGithub \
&& sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- --yes




