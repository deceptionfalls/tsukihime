#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#start sxhkd to replace Qtile native key-bindings
run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

#start mpd
[ ! -s ~/.config/mpd/pid ] && mpd &
mpd-notification &
mpd-rich-presence &
mpc &

clipmenud &
dunst &
#starting utility applications at boot time
picom --config $HOME/.config/picom.conf --vsync &
nitrogen --restore &
