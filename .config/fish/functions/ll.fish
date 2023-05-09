function ll --wraps='exa -l --color=always --group-directories-first' --description 'alias ll=exa -l --color=always --group-directories-first'
  exa -l --color=always --group-directories-first $argv
        
end
