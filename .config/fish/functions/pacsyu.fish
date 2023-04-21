function pacsyu --wraps='sudo pacman -Syu' --description 'alias pacsyu=sudo pacman -Syu'
  sudo pacman -Syu $argv
        
end
