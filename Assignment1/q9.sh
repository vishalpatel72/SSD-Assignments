#! /bin/bash


    read n
number=$(echo $n | tr -d " ")
len=${#number}
if((len<=1))
then
echo "invalid"
else
    pos=1
    sum=0
    for ((i=len-1;i>=0;i--)){
     d=${number:$i:1}

    if [[ $pos -eq 1 ]]; then
            sum=$(( sum + $d ))

            else
            x=0
            x=$((2*$d))
            sum=$((sum + ($x/10)))
            sum=$((sum + ($x%10)))
            fi
 
        pos=$(( ! $pos ))

    }
    rem=$((sum%10))
    if [[ $rem -eq 0 ]]; then
    echo "valid"
    else 
    echo "invalid"

fi
fi
