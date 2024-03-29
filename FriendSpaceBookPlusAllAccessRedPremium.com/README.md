

Downloading the zip file from the FriendSpaceBookPlusAllAccessRedPremium.com challenge and unzipping it gives 2 files:

- vm.py
- program

Looking into the program file I see that it contains emoticons in patterns. When opening the vm.py file we find a python script that expects the emoticon program as input and steps through it to execute some functions.

When running "python vm.py program" the first part of the text comes fast. It is clear that you will get some URL to follow. After some characters the next characters begin to come in slower and slower until its just not an option anymore to keep it running.

This challenge took quite a bit longer than I had hoped to spend on it.

I spend some time reading the vm.py code and I internalized the program as follows:

- The program creates a stack and 2 registers (medallions).
- It can load numbers (number emoticons) into registers.
- It can push what is in registers into the stack
- It can pop a number from the stack just throwing it out
- It can pop a number from the stack into any of the registers
- It can pop 2 numbers and do addition, subtraction, multiplication, division, modulo and xor
- It can duplicate the last value on the stack
- It can execute jumps to different locations
- It can run code or skip code if the last value on the stack is 0 or not 0
- It can change the pointer to an address based on the last value of the stack
- It can print the chr version of the last number on the stack

I had been doing some assembly reverse engineering exercises before the Google ctf so I thought ok this is just like assembly. Lets go over the instructions and see what is going on.

At first reading emoticon was very difficult and confusing. So I started fiddling with the vm.py file. As the code was running increasingly more slowly I thought that perhaps the challenge was to improve the vm.py code to be more efficient. I stayed on that thought for far to long. Even when it was clear that the vm code was not vastly improvable I still thought maybe the emoticon program file could be adjusted to avoid some loops.

This path of thinking made me spend a lot of time in emoticon land. After a while it even became easy to read what was going on. That is when I started realizing that this code was chuck full of jump and if_zero conditions that contained jumps.

I did find out that the 3 loading parts all had the same parsing of there generated stack below them so I tried splitting them in 3 and running each part separately with the vm. The second and third part however still never even gave one character output :(

I had during this time also already printed the stack on every step and noticed that there was a ton of steps involved in the longer taking parts. I had tough also noticed that the printing of a character was always preceded by an xor of one of the stack numbers loaded at the very start of program and a prime number. The prime numbers were going 2 3 5 7 11 101? 131 151 181 191??

At this point I was very close to solving it a lot faster than I ended up doing. As I could see that it was not using all prime numbers once past 11, I was thinking I now understood the challenge: Reverse the program code that generates certain prime numbers!

I still thought that maybe the program code could generate these primes without the amount of loops that it goes trough. After getting cross eyed and quite angry that I could not make any sense past the 5th what the algorithm was doing exactly and getting more and more the feeling that every loop did have a function that could not be skipped I finally gave up on the idea.

After this solving the challenge went quite fast and became fun again!! :D

typing in the primes 3 5 7 11 101 131 151 181 191? into Google in hope that it could tell me the pattern (I often refrain from putting parts of a challenge into Google as I fear to be spoiled by write-ups) I finally found out that these were all palindromic prime numbers!

I finally was there. Just lookup a list of these numbers and start xoring them with the loaded numbers. I used this page: https://prime-numbers.info/list/palindromic-primes

This made it possible for me to solve the first 2 blocks of the stack resulting in: http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com/

from just running the code while my struggles where going on I already got http://emoji-t0anaxnr3nacpt4na.web.ctfc and because I had already gotten to other challenges that had the .web.ctfcompetition.com/ domain I had guessed that part long before. I found the cats web page and while amusing to look trough I was quite convinced that this part would not get me to solve the challenge. I had counted the stack lines loaded and the chars in the URL and knew there was more to be decoded.

The last block was a small and fun obstacle. I could not find any pages that had enough of the palindromic prime numbers listed to solve it the easy way. I did find a page that had primes bigger than the ones in the stack of the last block. I created a small script (available here as vm_solver.py) to scrape these pages and filter out the palindromes. Then xored the results.

2 letters where not working. But are easily guessable. With this the full page revealed itself and with a few clicks there was that beautiful flag!! :D

It was a painful and long process but getting there in the end did feel very rewarding and creating some scripts for the last part was very calming. So in the end I did find this a really fun challenge and I feel like I learned a lot even during all the time I was stuck.
