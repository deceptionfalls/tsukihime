function newtag --wraps='git tag -a' --description 'alias newtag=git tag -a'
  git tag -a $argv
        
end
