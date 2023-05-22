if status is-interactive
  colorscript random
end

starship init fish | source

### 'bat' as manpager
set -x MANPAGER "sh -c 'col -bx | bat -l man -p'"
