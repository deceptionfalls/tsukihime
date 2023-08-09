#!/bin/sh

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# start mpd
[ ! -s ~/.config/mpd/pid ] && mpd &

./../.fehbg &
xfce4-power-manager &
xsettingsd &
dunst &
picom --config $HOME/.config/picom.conf &
