function mirrors --wraps='sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist' --description 'alias mirrors=sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist'
  sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist $argv
        
end
