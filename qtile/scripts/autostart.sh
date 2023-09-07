#!/bin/sh

# Autostart script
# the usual bash script to start apps

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

setxkbmap br & # keyboard layout
[ ! -s ~/.config/mpd/pid ] && mpd &
xfce4-power-manager &
xsettingsd &
dunst &
picom --config $HOME/.config/picom.conf &
