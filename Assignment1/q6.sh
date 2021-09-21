#!/bin/bash

array=( "$@" )
arraylength=${#array[@]}
res=$1
for (( i=1; i<${arraylength}; i++ ))
do
   res=$(($res**${array[$i]}))
done

echo $res