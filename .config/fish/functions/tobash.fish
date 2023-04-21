function tobash --wraps=sudo\ chsh\ tsukki\ -s\ /bin/bash\ \&\&\ echo\ \'Now\ log\ out.\' --description alias\ tobash=sudo\ chsh\ tsukki\ -s\ /bin/bash\ \&\&\ echo\ \'Now\ log\ out.\'
  sudo chsh tsukki -s /bin/bash && echo 'Now log out.' $argv
        
end
