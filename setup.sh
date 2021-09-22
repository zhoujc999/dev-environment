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
  python3 \
  software-properties-common \
  locales \
&& apt-get install -y fish \
&& locale-gen en_US.UTF-8 \
&& update-locale LANG=en_US.UTF-8 \
&& rm -rf /var/lib/apt/lists/*
