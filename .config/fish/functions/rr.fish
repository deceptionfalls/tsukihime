function rr --wraps='curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash' --description 'alias rr=curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash'
  curl -s -L https://raw.githubusercontent.com/keroserene/rickrollrc/master/roll.sh | bash $argv
        
end
