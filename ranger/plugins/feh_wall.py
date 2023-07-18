import os
from ranger.api.commands import Command

class feh_wall(Command):
    def execute(self):
        if self.fm.thisfile.extension in ('jpg', 'jpeg', 'png', 'bmp', 'gif'):
            image_path = self.fm.thisfile.path
            os.system(f'feh --bg-fill {image_path}')
            self.fm.notify('Wallpaper set successfully!')
        else:
            self.fm.notify('Selected file is not an image.')
