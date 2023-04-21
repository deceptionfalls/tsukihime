#!/usr/bin/env bash

# Color files
PFILE="$HOME/.config/polybar/blocks/colors.ini"
RFILE="$HOME/.config/polybar/blocks/scripts/rofi/colors.rasi"

# Change colors
change_color() {
	# polybar
	sed -i -e "s/background = #.*/background = $BG/g" $PFILE
	sed -i -e "s/background-alt = #.*/background-alt = $BGA/g" $PFILE
	sed -i -e "s/foreground = #.*/foreground = $FG/g" $PFILE
	sed -i -e "s/foreground-alt = #.*/foreground-alt = $FGA/g" $PFILE
	sed -i -e "s/primary = #.*/primary = $AC/g" $PFILE
	
	# rofi
	cat > $RFILE <<- EOF
	/* colors */

	* {
	  al:   #00000000;
	  bg:   ${BG}FF;
	  bga:  ${BGA}FF;
	  fga:  ${FGA}FF;
	  fg:   ${FG}FF;
	  ac:   ${AC}FF;
	  se:   ${AC}40;
	}
	EOF
	
	polybar-msg cmd restart
}

if  [[ $1 = "--default" ]]; then
	BG="#24273a"
	BGA="#1e2030"
	FGA="#5b6078"
	FG="#cad3f5"
	AC="#b7bdf8"
	change_color
elif  [[ $1 = "--nord" ]]; then
	BG="#24273a"
	BGA="#1e2030"
	FGA="#5b6078"
	FG="#cad3f5"
	AC="#b7bdf8"
	change_color
elif  [[ $1 = "--gruvbox" ]]; then
	BG="#24273a"
	BGA="#1e2030"
	FGA="#5b6078"
	FG="#cad3f5"
	AC="#b7bdf8"
	change_color
elif  [[ $1 = "--adapta" ]]; then
	BG="#24273a"
	BGA="#1e2030"
	FGA="#5b6078"
	FG="#cad3f5"
	AC="#b7bdf8"
	change_color
elif  [[ $1 = "--cherry" ]]; then
	BG="#24273a"
	BGA="#1e2030"
	FGA="#5b6078"
	FG="#cad3f5"
	AC="#b7bdf8"
	change_color
else
	cat <<- _EOF_
	No option specified, Available options:
	--default    --nord    --gruvbox    --adapta    --cherry
	_EOF_
fi
