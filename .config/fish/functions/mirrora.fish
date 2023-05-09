function mirrora --wraps='sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist' --description 'alias mirrora=sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist'
  sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist $argv
        
end
