function cleanup --wraps='sudo pacman -Rns $(pacman -Qtdq)' --description 'alias cleanup=sudo pacman -Rns $(pacman -Qtdq)'
  sudo pacman -Rns $(pacman -Qtdq) $argv
        
end
