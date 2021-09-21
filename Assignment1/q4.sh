#1 /bin/bash


read a

  b=$( echo $a |tr -s '()' ' ' )
   
   echo "($b)"
   

   