
# Assignment-1


### Question-1
   - I assumed `home` as my defualt location to create Assignment1 directory.
   touch command to create `lab.txt` files.
  - ls.`*txt` to list all `.txt` files then pipe the content of `ls.*txt` to  `xargs -I` to pass the  file name to `mv` command which it will change all `.txt` files to `.c` files.
   - `ls -laShr` => to sort in increasing order of the size in human readable format.
   - `find -max depth 2 ` will display all files within the depth of 2nd level
   - `find "$(pwd)" -name "*.txt` => to display all files with extension ".txt" from the current Directory.
 
  

### Question-2 
  - All bash commands is taken in array named as `array_of_commands` and then sorted every command and put all sorted commands into array named as `sorted_array`.
  - I also sorted user input command also and then compare input command with array of `sorted_array` commands if any of the command matches then it will display "Yes" as well as name of the standard command.
  
  
### Question-3
   - `cat ~/.bash_history` =>this command displays History of standard Bash commands
   - `uniq -c` command to combine all the similar commands from last 10 used commands and also the count of specified command then pipe it with `sort -r`
   - to sort in descending order of count then print "command name"+"frequency" by using `awk`.
   
   
### Question-4
  - `pipe` the user input to `tr` with `-s` option, and convert the `'('` `')'` into `" "`.
   

### Question-5
 - `word=${word,,}` => is used to convert "input word" into "lower case" and then reverse the word using `rev` command and then compare "reverse of the word" with the value of "word".if it matches print "Yes" otherwise print "No".
 
 ### Question-6
  - Take all command line User input to "array".
  - then store `$1'( first command line input) into res variable then iterate over the loop 
  - applied logic in for loop and store the result in `res`
 variable and when loop terminate echo the value of the `res` variable.


### Question-7
  - `ps -au` gives all running process in sorted by `PIDs`and store it in 'pid.txt' file 
  - `pid.txt` is created by assuming "home" is default location to store file.
  - `awk` displays the all "PIDs" with column nume "PID".
  - `sed '1d'` is used to remove "PID" column name.
  - `head -n $N` gives first "N" PIDs.
  
### Question-8
 - To run this script,you should have `crontab_file` saved in current directory.
 -  format will be aytomatically validated by running `crontab`command on the `crontab_file` and redirect the output to the variable `n`.
 -  we check the `nullity` of a variable `n` by using `-z $n` if incase it  returns teue then print "Yes" otherwise "No".
  
  
### Question -9
  - read input from user
  - then remove blank spaces from input string by using `tr -d " "`.
  - then applied simple logic of `lun Algorithm` to check given card number is valid or not.
  
  
### Question-10
   - applied simple logic to implement "basic calculator"
   - For Multiplication and division operation,output is displayed with 4 decimal precision.
   