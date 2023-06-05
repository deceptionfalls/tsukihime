if status is-interactive
  pokemon-colorscripts -r -s
end

starship init fish | source

### 'bat' as manpager
set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"
