#! /bin/bash

read comm
array_of_commands=("alias" "apropos" "apt-get" "aptitude" "aspell" "awk" "basename" "base32" "base64" "bash" "bc" "bg" "bind" "break" "builtin" "bzip2" "cal" "case" "cat" "cd" "cfdisk" "chattr" "chgrp" "chmod" "chown" "chpasswd" "chroot" "chkconfig" "cksum" "clear" "cmp" "comm" "command" "continue" "cp" "cpio" "cron" "crontab" "csplit" "curl" "cut" "date" "dc" "dd" "ddrescue" "declare" "df" "diff" "diff3" "dig" "dir" "dircolors" "dirname" "dirs" "dmesg" "du" "echo" "egrep" "eject" "enable" "env" "ethtool" "eval" "exec" "exit" "expect" "expand" "export" "expr" "false" "fdformat" "fdisk" "fg" "fgrep" "file" "find" "fmt" "fold" "for" "format" "free" "fsck" "ftp" "function" "fuser" "gawk" "getopts" "grep" "groupadd" "groupdel" "groupmod" "groups" "gzip" "hash" "head" "help" "history" "hostname" "htop" "iconv" "id" "if" "ifconfig" "ifdown" "ifup" "import" "install" "iostat" "ip" "jobs" "join" "kill" "killall" "less" "let" "link" "ln" "local" "locate" "logname" "logout" "look" "lpc" "lpr" "lprint" "lprintd" "lprintq" "lprm" "lsattr" "lsblk" "ls" "lsof" "lspci" "make" "man" "mapfile" "mkdir" "mkfifo" "mkfile" "mkisofs" "mknod" "mktemp" "more" "most" "mount" "mtools" "mtr" "mv" "mmv" "nc" "netstat" "nft" "nice" "nl" "nohup" "notify-send" "nslookup" "open" "op" "passwd" "paste" "pathchk" "Perf" "ping" "pgrep" "pkill" "popd" "pr" "printcap" "printenv" "printf" "ps" "pushd" "pv" "pwd" "quota" "quotacheck" "ram" "rar" "rcp" "read" "readarray" "readonly" "reboot" "rename" "renice" "remsync" "return" "rev" "rm" "rmdir" "rsync" "screen" "scp" "sdiff" "sed" "select" "seq" "set" "sftp" "shift" "shopt" "shutdown" "sleep" "slocate" "sort" "source" "split" "ss" "ssh" "stat" "strace" "su" "sudo" "sum" "suspend" "sync" "tail" "tar" "tee" "test" "time" "timeout" "times" "touch" "top" "tput" "traceroute" "trap" "tr" "true" "tsort" "tty" "type" "ulimit" "umask" "umount" "unalias" "uname" "unexpand" "uniq" "units" "unrar" "unset" "unshar" "until" "uptime" "useradd" "userdel" "usermod" "users" "uuencode" "uudecode" "v" "vdir" "vi" "vmstat" "w" "wait" "watch" "wc" "whereis" "which" "while" "who" "whoami" "wget" "write" "xargs" "xdg-open" "xz" "yes" "zip" "else" "do" "then" "elif" "done" "in" "coproc" "alert" "typeset" "disown" "complete" "caller" "compgen")

sorted_array=(aails aoopprs -aegptt adeipttu aellps akw aabeemns 23abes 46abes abhs bc bg bdin abekr biilntu 2bipz acl aces act cd cdfiks achrtt cghpr cdhmo chnow acdhpssw choort ccfghikno ckmsu acelr cmp cmmo acdmmno ceinnotu cp ciop cnor abcnort cilpst clru ctu adet cd dd cddeersu acdeelr df dffi 3dffi dgi dir cdiloorrs adeimnr dirs degms du ceho eegpr ceejt abeeln env ehloott aelv ceex eitx ceeptx adenpx eoprtx eprx aefls adffmort dfiks fg efgpr efil dfin fmt dflo for afmort eefr cfks fpt cfinnotu efrsu agkw egopstt egpr addgopru deglopru dgmoopru goprsu gipz ahhs adeh ehlp hiorsty aehmnost hopt cinov di fi cffgiino dfinow fipu imoprt aillnst aiostt ip bjos ijno ikll aikllll elss elt ikln ln acllo acelot aeglmno glootu kloo clp lpr ilnprt dilnprt ilnpqrt lmpr alrstt bklls ls flos cilps aekm amn aefilmp dikmr ffikmo efiklm fikmoss dkmno ekmmpt emor most mnotu lmoost mrt mv mmv cn aensttt fnt cein ln hnopu -definnosty klnoopsu enop op adpssw aepst achhkpt efPr ginp egppr ikllp dopp pr acinpprt einnprtv finprt ps dhpsu pv dpw aoqtu accehkoqtu amr arr cpr ader aaaderrry adelnory beoort aeemnr ceeinr cemnrsy enrrtu erv mr dimrr cnrsy ceenrs cps dffis des ceelst eqs est fpst fhist hopst dhnostuw eelps acelost orst ceorsu ilpst ss hss astt acerst su dosu msu denpssu cnsy ailt art eet estt eimt eimottu eimst chotu opt pttu aceeorrttu aprt rt ertu orstt tty epty iilmtu akmsu mnotuu aailnsu aemnu adennpux inqu instu anrru enstu ahnrsu ilntu eimptu addersu deelrsu demorsu erssu cdeenouu cddeeouu v dirv iv amsttv w aitw achtw cw eehirsw chhiw ehilw how ahimow egtw eirtw agrsx -degnopx xz esy ipz eels "do" ehnt eifl deno "in" ccoopr aelrt eepstty dionsw ceelmopt acellr cegmnop)

n=${#sorted_array[@]}

sort_comm=$(echo $comm | grep -o . | sort | tr -d "\n")

count=0
j=0

for (( i=0; i<n; i++)) 
do
if [ $sort_comm = ${sorted_array[i]} ]
then 
y=${array_of_commands[j]}
count=1
fi
((j++))
done

if (($count==1))
then
echo "Yes"
echo $y
else
echo "No"
fi