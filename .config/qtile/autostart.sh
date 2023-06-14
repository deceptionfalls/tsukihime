#!/usr/bin/env bash 

dunst &
mpd &
mpd-notification &
mpc &

killall picom
picom &

/usr/bin/emacs --daemon &
nitrogen --restore &
sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &
