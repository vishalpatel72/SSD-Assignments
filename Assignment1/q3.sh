#! /bin/bash



cat ~/.bash_history | tail -n10 | awk '{print $1}'| sort -n | uniq -c | sort -r | awk '{print $2 " " $1}'