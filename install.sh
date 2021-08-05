#!/usr/bin/env bash

apt-get update \
&& apt-get install -y \
  software-properties-common \
  locales \
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
&& apt-add-repository ppa:fish-shell/release-3 \
&& apt-get update \
&& apt-get install -y fish \
&& rm -rf /var/lib/apt/lists/* \
&& locale-gen en_US.UTF-8 \
&& update-locale LANG=en_US.UTF-8 \
&& sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- --yes \
&& curl -L https://raw.githubusercontent.com/tj/n/master/bin/n -o n \
&& bash n lts





