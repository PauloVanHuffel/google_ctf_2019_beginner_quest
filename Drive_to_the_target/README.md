the drive to the target challenge is a coding challenge.

We get a link to a webpage where we can change coordinates and then go to this location. <br />
Playing a bit with the web page manualy we observe the following:
- making large jumps gives a message that we go to fast and sets the location back to the one before
- making a small move in the right direction for both x and y tells me i'm getting closer
- making a small move in the wrong direction for both x and y tells me i'm getting away.

The reason you need to code this is thus that you can only make small incremental steps.

To solve this I made a program where i scrape the webpage with beautiful soup. <br />
The parts I need are the current lat and lon values and there is a token. This token is what makes sure I did not make large jump since the last page.<br />
For the next page I need to make a get request to the same page with:<br />
?lat=\<new lat\>&lon=\<new lon\>&token=\<Token form last page\><br />

I wonder on what this token hash is made. I'm guessing based on the lat and lon and maybe something else. You might be able to hack this and figure out a token that alows for large jumps but it did not seem worth it to investigate further.

So for the program I just made a while loop that takes small steps in the correct lat or lon direction (gotten from manual probe) until I get the message i am getting away<br />
I then adjusted the program to do the same for the other (lat or lon) direction and started of from the token of where my while loop stopped.

Doing this I eventualy got to the location where I needed to be and got the flag.

I personaly did not find this challange very exciting for being an ending to a ctf path as it did not require very special programming.

The code with this is thus not in the most clean state as I adjusted it midway to do the other half and did not bother to make it better with clean functions to get from start to end in one go as I found the challenge a bit boring. running the code will make it start from midway and go to the solution as it has the token for the first part hardcoded in it.
