function remove --wraps='sudo pacman -R' --description 'alias remove=sudo pacman -R'
  sudo pacman -R $argv
        
end
