function commit --wraps='git commit -m' --description 'alias commit=git commit -m'
  git commit -m $argv
        
end
