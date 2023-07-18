import os
from ranger.api.commands import Command

class set_lockscreen_wallpaper(Command):
    def execute(self):
        if self.fm.thisfile.extension in ('jpg', 'jpeg', 'png', 'bmp' ):
            image_path = self.fm.thisfile.path
            os.system(f'betterlockscreen -u {image_path} > /dev/null 2&>1')
            self.fm.notify('Lockscreen wallpaper set successfully!')
        else:
            self.fm.notify('Selected file is not an image.')

