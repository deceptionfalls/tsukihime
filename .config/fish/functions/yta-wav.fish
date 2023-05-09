function yta-wav --wraps='youtube-dl --extract-audio --audio-format wav ' --description 'alias yta-wav=youtube-dl --extract-audio --audio-format wav '
  youtube-dl --extract-audio --audio-format wav  $argv
        
end
