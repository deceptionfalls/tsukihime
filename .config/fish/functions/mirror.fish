function mirror --wraps='sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist' --description 'alias mirror=sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist'
  sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist $argv
        
end
