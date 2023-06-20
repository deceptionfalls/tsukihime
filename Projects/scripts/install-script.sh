#!/usr/bin/env bash

pkgs=(
  neovim
  mpd
  mpv
  mpc
  ncmpcpp
  exa
  bat
  bat-extras
  fish
  git
  rofi
  dunst
  python
  firefox
  sxhkd
  qview
  ranger
  npm
  flatpak
  nodejs
  neofetch
  lua
  )
sudo pacman -S "${pkgs[@]}"
