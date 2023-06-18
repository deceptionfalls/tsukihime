#!/usr/bin/env bash

sleep 0.2

value="$(xset q | grep -i caps | cut -c 22-24)"

if [ $value == "on" ];
    then
        output="Caps Lock is On"
    else
        output="Caps Lock is Off"
fi

notify-send -t 1150 "$output"
