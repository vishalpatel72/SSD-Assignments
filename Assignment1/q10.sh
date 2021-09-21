#!/bin/bash

read operator
read n


if [ " $operator " = " + " ] ; then
read b
for((i=0;i<n-1;i++))
do
read a
   b=$(echo "$b+$a" |bc);
done
echo $b
fi



if [ " $operator " = " - " ] ; then
read b
for((i=0;i<n-1;i++))
do
read a
   b=$(echo "$b-$a" |bc);
done
echo $b
fi



if [ " $operator " = " * " ] ; then
read b
for((i=0;i<n-1;i++))
do
read a
   b=$(echo "scale=4;$b*$a" |bc);
done
echo $b
fi



if [ " $operator " = " / " ] ; then
read b
for((i=0;i<n-1;i++))
do
read a
   b=$(echo "scale=4;$b/$a" |bc);
done
echo $b
fi
