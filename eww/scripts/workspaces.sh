#!/bin/bash 

# this is for sway!!! make sure to change to dir!!!

$HOME/.config/eww/copy_oxocarbon/scripts/workspace.py
while [ 1 == 1 ] ; do
    swaymsg -t subscribe '["workspace"]' > /dev/null
    $HOME/.config/eww/copy_oxocarbon/scripts/workspace.py
done
