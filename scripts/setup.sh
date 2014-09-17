#!/bin/bash

if [[ $# -lt 2 ]]
then
  echo ""
  echo "     USAGE: ./setup.sh [StudentID name]"
  echo "        ex: ./setup.sh 12345678 David Weintrop"
  echo ""
  exit
fi

# grab student ID
ID=$1
shift

NAME=$1
shift
#grab student name
while [[ $# -ge 1 ]]
do
  NAME="$NAME $1"
  shift
done

# Download the appropriate compiler for the user's shell
if [[ "$SHELL" = '/bin/bash' ]]
then
  curl -k https://raw.githubusercontent.com/dweintrop/javaseer/master/scripts/javaseer.sh -o ~/javaseer.sh
  echo 'alias javac="~/javaseer.sh"' >> ~/.bash_profile
  echo "export STUDENT_ID=\"$ID\"" >> ~/.bash_profile
  echo "export STUDENT_NAME=\"$NAME\"" >> ~/.bash_profile
  echo "export JAVASEER_URL=\"http://javaseer.herokuapp.com\"" >> ~/.bash_profile
  echo "alias has been setup. please close then reopen the terminal"
else
  echo "this user's shell isn't BASH"
  echo "no setup was performed"
  exit
fi

# Make the research compiler executable
chmod 700 ~/javaseer.sh
