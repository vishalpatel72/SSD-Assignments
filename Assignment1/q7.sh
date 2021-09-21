#!/bin/bash
read N
ps -au > pid.txt
cat pid.txt | awk '{print $2}'| sed '1d' | head -n $N
