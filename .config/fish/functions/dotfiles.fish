function dotfiles --wraps='/usr/bin/git --git-dir=/home/tsukki/dotfiles --work-tree=/home/tsukki' --description 'alias config=/usr/bin/git --git-dir=/home/tsukki/dotfiles --work-tree=/home/tsukki'
  /usr/bin/git --git-dir=/home/tsukki/dotfiles --work-tree=/home/tsukki $argv
        
end
