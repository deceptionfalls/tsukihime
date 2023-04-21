function unlock --wraps='sudo rm /var/lib/pacman/db.lck' --description 'alias unlock=sudo rm /var/lib/pacman/db.lck'
  sudo rm /var/lib/pacman/db.lck $argv
        
end
