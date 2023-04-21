function tozsh --wraps=sudo\ chsh\ tsukki\ -s\ /bin/zsh\ \&\&\ echo\ \'Now\ log\ out.\' --description alias\ tozsh=sudo\ chsh\ tsukki\ -s\ /bin/zsh\ \&\&\ echo\ \'Now\ log\ out.\'
  sudo chsh tsukki -s /bin/zsh && echo 'Now log out.' $argv
        
end
