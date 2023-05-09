function ytv-best --wraps='youtube-dl -f bestvideo+bestaudio ' --description 'alias ytv-best=youtube-dl -f bestvideo+bestaudio '
  youtube-dl -f bestvideo+bestaudio  $argv
        
end
