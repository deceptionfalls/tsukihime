#!/usr/bin/env bash

pkgs=(
  firefox
  alacritty
  fish
  exa
  bat
  bat-extras
  neovim
  mpd
  mpv
  mpc
  ncmpcpp
  rofi
  dunst
  python
  sxhkd
  ranger
  npm
  flatpak
  nodejs
  neofetch
  lua
  tmux
  picom
  starship
  qview
  )
# get yay
sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
yay -S "${pkgs[@]}"
