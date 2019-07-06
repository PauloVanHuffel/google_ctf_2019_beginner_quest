In this challenge we get a adres to netcat to.<br />
When we do so we get a terminal. doing ls -al shows 2 files:
- ORME.flag
- README.flag

Trying cat README.flag shows cat is not installed. Here I realize this is one of those challenges where you need to figure out how to print the files.

Some extra info about the files: <br />
the ORME.flag has permissions 000. This is the first time i encounter this as I have never had any practical use for this setting. fascenating tough. <br />
The second file is read only for the file creator: pid 1338

The result of whoami shows us we are 1338 so we wont be needing privilege escalation to root to reed the README.flag file.<br />
For the ORME.flag there are 2 options. either we get to change the file permissions or we need to do privilege escalation to root to read it.

To find out what programs I could use to print the files I look into these folders:
- /bin
- /usr/bin

so ls -al /bin and ls -al /usr/bin

I see that there is this /bin/busybox program and all other programs are symlinks to this program. I did not know busybox. <br />
When i try to run busybox itself I get the following message:<br />
busybox can not be called for alien reasons.

At the first time it had not occured to me that the use of alien here is fairly strange and is very fitting for the CTF story.<br />
I let this go for a bit and tried some other tools.

After sifting trough the functions and calling them with --help if they seem promising I first stumbled on the split command.<br />
I looked around a bit if split could output to stdout but I did not get that working. What i did find out is that README.flag only has one line as splitting on every 1 line resulted in 1 output file.

A bit later I came acros the shuf command. I had never used this command but the help told me it randomly permutates lines. One of the options is write to file, not to standard output. AHA! <br />

using shuf REAMD.flag we get the first flag!

I left the second flag for what is and continued with the other challenges but later came back to this.

Eventualy I googled what this busybox was and found out this was a command that could be used to run almost all other standard linux commands like cat and chmod that I was needing. Now I finaly realized this alien reference and this convinced me this was the path that would get me to the solution.

So busybox did not let me access it with the current user. I needed some escalation but I might not need to be root unless all other users where also aliens.

I tried to check if there was any cronjobs running by regularly running ps aux but did not see anything. I tried to use watch to vastly increase the likelyhood of seeing something but this did not seem to work and I did not try to figure it out as I was starting to feel this was a dead end.

The busybox commands all seemed to be the standard linux commands and it did not seem likely to find a bug there. The non busybox commands however did not seem to be mutch better candidates. The only program I saw was /bin/shell which just spawns a new clean shell when ran. Any parameters given does not seem to affect it and there is no --help output.

Eventualy I see the setpriv command. the --help does not realy clarify how it functions but setpriv busybox does give me the help message. yeay i guess. Using setpriv whoami i'm still the same user so I accualy still don't know why this works which realy bugs me. <br />

I now ran run setpriv busybox chmod u+r ORME.flag and use busybox cat or shuf again to print the flag!

Further googling tells me setpriv drops privileges so I think I dropped from alien to lower but I still don't know what I drop into and why and how this difference changes my acces to busybox apart from it no longer thinking I'm an alien.. but why?

