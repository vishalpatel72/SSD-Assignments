#! /bin/bash

mkdir Assignment1
cd Assignment1/
touch lab1.txt touch lab2.txt touch lab3.txt touch lab4.txt touch lab5.txt
ls *.txt | xargs -I {} bash -c 'mv "$1" "${1%.txt}.c"' -- {}
ls -laShr 
cd
find ~ -maxdepth 2
cd Assignment1/
find "$(pwd)" -name "*.txt"
