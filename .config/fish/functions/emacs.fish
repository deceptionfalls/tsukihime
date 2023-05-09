function emacs --wraps=emacsclient\ -c\ -a\ \'emacs\' --description alias\ emacs=emacsclient\ -c\ -a\ \'emacs\'
  emacsclient -c -a 'emacs' $argv
        
end
