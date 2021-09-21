#!/bin/bash

n=$(crontab "$1" 2>&1)

if [[ -z "$n" ]]
then
echo "Yes"
else
echo "No"
fi
