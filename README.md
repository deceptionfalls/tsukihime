# Dotfiles
![](https://raw.githubusercontent.com/tsukki9696/dotfiles/main/le%20rice.png)

My personal dotfiles repository. The purpose of this repository is to function as both a backup and as a way for people to freely inspect my configs. Some of the files here are for mostly, my personal use but anyone can freely clone this repository to use it as they see fit. Many configs here can change time to time, and what I use may change as well.

### My current programs
- **Window Manager**: Qtile
- **Terminal Emulator**: Wezterm
- **Text Editor**: Nvim
- **App Launcher**: Rofi
- **File Explorer**: PCmanFM(GUI), `ranger`(TUI)
- **Shell**: `zsh`
- **Music Player**: `mpd` with `ncmpcpp` as a client
- **neofetch**: for checking specs.

### Pywal
My current `pywal` setup is a bit cumbersome, I have a custom ranger plugin to setup a wallpaper, reload dunst, qtile and my GTK theme (powered by Oomox), but it should work in your machine as well.

### Setup
This repo comes with a `install-script.sh` script that installs most dependencies for the programs I use. This script also will install `yay` and has a prompt for copying wallpapers from my wallpapers repository. 

> You are encouraged to tinker with the script and tailor what you want and don't want to be installed, the script automatically bypass packages you have installed already. All packages come from the Arch User Repository, you might want to tinker with it to include packages from your distro's repository.

```bash
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
```

## Questions

### How do I setup polybar?
`bash ~/.config/polybar/launch.sh --blocks` should work.

### Where can I find the wallpapers you use?
https://github.com/tsukki9696/wallpapers contains everything that I use (none of the wallpapers are mine and I do not claim ownership of them).

