#!/usr/bin/env bash

#  _____          _    _    _ _       ___           _        _ _
# |_   _|__ _   _| | _| | _(_| )___  |_ _|_ __  ___| |_ __ _| | |
#   | |/ __| | | | |/ / |/ / |// __|  | || '_ \/ __| __/ _` | | |
#   | |\__ \ |_| |   <|   <| | \__ \  | || | | \__ \ || (_| | | |
#   |_||___/\__,_|_|\_\_|\_\_| |___/ |___|_| |_|___/\__\__,_|_|_|
#  ____            _       _           _
# / ___|  ___ _ __(_)_ __ | |_  __   _/ |
# \___ \ / __| '__| | '_ \| __| \ \ / / |
#  ___) | (__| |  | | |_) | |_   \ V /| |
# |____/ \___|_|  |_| .__/ \__|   \_/ |_|
#                   |_|

# This script is meant to install most of the applications that I run currently.
# I recommend you fine tune this script to suit your needs and install what you want.
# Some WMs and apps like polybar aren't added because I don't use them anymore
# But you can uncomment and comment what you want and don't want to install.

# List of packages
# Insert what you wanna install here

pkgs=(
  # Core utils
  firefox
  alacritty
  fish
  dunst
  ranger
  flatpak
  qview
  neovim
  ufw
  # Langs
  lua
  nodejs
  npm
  python
  # Leisure
  mpd
  mpv
  mpc
  ncmpcpp
  neofetch
  # Other tools
  sxhkd
  tmux
  picom
  starship
  exa
  bat
  bat-extras
  rofi
  p7zip
  # Qtile dependencies
  python-wifi
  python-mpd2
  python-dbus-next
  python-requests
  python-cffi
  wireless_tools
  python-setuptools
  python-pytest
  python-iwlib
  python-psutil
  )

# Define commands
pacman_cmd="sudo pacman -S --needed"
yay_url="https://aur.archlinux.org/yay.git"
yay_dir="yay"
wallpapers_repo="https://github.com/tsukki9696/wallpapers"

# Function to show error notification
show_error_notification() {
  notify-send -u critical -t 5000 "Installation Error" "$1"
}

show_info_notification() {
  notify-send -u normal -t 3000 "$1"
}

# Prompt for installing wallpapers
read -rp "Do you want to install wallpapers from the git repository? [Y/n]: " install_wallpapers

if [[ $install_wallpapers =~ ^[Yy]$ ]]; then
  # Clone wallpapers repository
  git clone "$wallpapers_repo" || { show_error_notification "Failed to clone wallpapers repository."; exit 1; }
  show_info_notification "Wallpapers added"
fi

# Install yay if not already installed
if ! command -v yay &>/dev/null; then
  $pacman_cmd git base-devel || { show_error_notification "Failed to install required packages."; exit 1; }
  git clone "$yay_url" || { show_error_notification "Failed to clone yay repository."; exit 1; }
  cd "$yay_dir" && makepkg -si || { show_error_notification "Failed to build and install yay."; exit 1; }
  cd ..
fi

# Install packages
yay -S "${pkgs[@]}" || { show_error_notification "Failed to install packages with yay or script was aborted."; exit 1; }

# Script finished successfully
show_info_notification "Script finished"
