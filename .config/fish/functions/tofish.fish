function tofish --wraps=sudo\ chsh\ tsukki\ -s\ /bin/fish\ \&\&\ echo\ \'Now\ log\ out.\' --description alias\ tofish=sudo\ chsh\ tsukki\ -s\ /bin/fish\ \&\&\ echo\ \'Now\ log\ out.\'
  sudo chsh tsukki -s /bin/fish && echo 'Now log out.' $argv
        
end
