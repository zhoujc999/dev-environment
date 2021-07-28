#!/usr/bin/env bash
apt-get update && apt-get install -y \
  tmux \
  git \
  curl \
  fd-find \
  ripgrep \
  vim \
  sudo \
  fish \
  && rm -rf /var/lib/apt/lists/*
