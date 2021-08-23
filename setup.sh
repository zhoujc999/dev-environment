#!/usr/bin/env bash

apt-get update \
&& apt-get install -y \
  sudo \
  curl \
  git \
  vim \
  tmux \
  fd-find \
  ripgrep \
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
&& rm -rf /var/lib/apt/lists/* \
&& python3 -m pip install PyGithub \

