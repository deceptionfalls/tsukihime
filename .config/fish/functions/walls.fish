function walls --wraps='/usr/bin/git --git-dir=$HOME/wallpaper/wallpaper.git/ --work-tree=$HOME' --description 'alias walls=/usr/bin/git --git-dir=$HOME/wallpaper/wallpaper.git/ --work-tree=$HOME'
  /usr/bin/git --git-dir=$HOME/wallpaper/wallpaper.git/ --work-tree=$HOME $argv
        
end
