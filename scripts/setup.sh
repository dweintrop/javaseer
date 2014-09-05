#!/usr/bin/tcsh

if ( "$1" == "" ) then
  echo ""
  echo "     USAGE: ./setup.sh [StudentID email]"
  echo "        ex: ./setup.sh 12345678 student@cps.edu"
  echo ""
  exit
endif

# Download the appropriate compiler for the user's shell
if ( "$SHELL" =~ *bash ) then
  curl -k https://https://raw.githubusercontent.com/dweintrop/javaseer/master/scripts/javaseer.sh -o ~/javaseer.sh
  echo 'alias javac="~/javaseer.sh"' >> ~/.bash_aliases
  source ~/.bash_aliases
  echo "alias has been setup."
# else if ( "$SHELL" =~ *tcsh* ) then
#   # tcsh version (UMD default shell)
#   curl -k https://raw.github.com/WilDoane/GitDataCollection/master/research-compiler-tcsh.sh -o ~/research-compiler.sh
#   echo 'alias gcc "~/research-compiler.sh"' >> ~/.aliases
#   source ~/.aliases
else
  echo "this user's shell isn't BASH"
  echo "no setup was performed"
  exit
endif

# Make the research compiler executable
chmod 700 ~/javaseer.sh

  