# Dotfiles
![](https://github.com/tsukki9696/dotfiles/blob/4599d991a0e7520889a12020f0d58cbd62145e05/2023-08-11_16-49.png)

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

### Setup
This repo comes with a `install-script.sh` script that installs most dependencies for the programs I use. This script also will install `yay` and has a prompt for copying wallpapers from my wallpapers repository. 

> You are encouraged to tinker with the script and tailor what you want and don't want to be installed, the script automatically bypass packages you have installed already. All packages come from the Arch User Repository, you might want to tinker with it to include packages from your distro's repository.

```bash
# List of packages
# Insert what you wanna install here

pkgs=(
    stuff you want here
)
```
