import os
from ranger.api.commands import Command

class set_wallpaper(Command):
    def execute(self):
        if self.fm.thisfile.extension in ('jpg', 'jpeg', 'png', 'bmp', 'gif'):
            image_path = self.fm.thisfile.path

            # Set wallpaper using wal -i and send output to /dev/null
            os.system(f'wal -i {image_path} > /dev/null 2>&1')

            # Execute pywalfox update and send output to /dev/null
            os.system('pywalfox update > /dev/null 2>&1')

            # Generate GTK theme using oomox-cli
            os.system('oomox-cli -m gtk2 -m gtk3 ~/.cache/wal/colors-oomox > /dev/null 2>&1')

            # Reload qtile configuration and send output to /dev/null
            os.system('qtile cmd-obj -o cmd -f reload_config > /dev/null 2>&1')

            # Execute dunst-pywal.sh script
            dunst_script_path = os.path.expanduser('~/.config/dunst/dunst-pywal.sh')
            os.system(f'bash {dunst_script_path} > /dev/null 2>&1')

            # Set GTK theme using xfconf-query
            theme_path = '/home/tsukki/.themes/oomox-colors-oomox'
            os.system(f'xfconf-query -c xfwm4 -p /general/theme -s {theme_path} > /dev/null 2>&1')

            self.fm.notify('Wallpaper set successfully!')
        else:
            self.fm.notify('Selected file is not an image.')
