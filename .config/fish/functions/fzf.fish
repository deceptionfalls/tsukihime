function fzf --description alias\ fzf=fzf\ --preview\ \'bat\ --color=always\ --style=numbers\ --line-range=:500\ \{\}\'
 command fzf --preview 'bat --color=always --style=numbers --line-range=:500 {}' $argv
        
end
