#!/usr/bin/env bash

apt-get update \
&& apt-get install -y \
  software-properties-common \
  locales \
  tmux \
  git \
  curl \
  fd-find \
  ripgrep \
  vim \
  bat \
  exa \
  fzf \
  sudo \
&& apt-add-repository ppa:fish-shell/release-3 \
&& apt-get update \
&& apt-get install -y \
  fish \
&& rm -rf /var/lib/apt/lists/* \
&& sh -c "$(curl -fsSL https://starship.rs/install.sh)" -- --yes





