
#! /bin/bash

read word
 
  word=${word,,}


if [[ $(rev <<< "$word") == "$word" ]]; then
    echo "Yes"
    else
    echo "No"
fi  