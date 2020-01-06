#!/bin/bash

echo -en "\e[36mReset git and make clean? (y/n) \e[0m"
read reply
case "$reply" in
  y|Y)
    # reset git
    if [[ -d .git ]]
    then
      rm -rf .git
    fi
    git init &> /dev/null
    
    # update readme
    if [[ $(head -n 1 README.md) == "## Fresh Start" ]]
    then
      sed -i "1,8d" README.md
    fi

    # cleanup python cache
    ./clean.sh
    
    echo -e "\e[32mGit repo re-initialized. \e[0m" 
    
    # remove fresh file
    rm -f fresh.sh
  ;;
  n|N)
    echo -e "\e[31mGit repo has not been reset. \e[0m"
  ;;
esac
