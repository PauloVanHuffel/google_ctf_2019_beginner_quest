In this challenge you get a pdf and a binary init_sat

as a quick check i tried to do
strings init_sat | grep CTF

As this was the solution for the very first chal I did not expect this to work and it did not.

In both the introductory text as in the pdf there is a reference to an "osmium" satellite.
When you run the ./init_sat binary (chmod +x to make it executable)
you are asked to give a satellite name so I entered osmium (i tried and different casings like OsMiUM also work)

this gives you an option to display some data.

which then gives you:
Username: brewtoot password: ********************
and a reference to a googe docs file containing:
VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==

the == at the end is a big indicator that this is a base64 encoded string so we decode it:

echo "VXNlcm5hbWU6IHdpcmVzaGFyay1yb2NrcwpQYXNzd29yZDogc3RhcnQtc25pZmZpbmchCg==" | base64 -d

result:
Username: wireshark-rocks
Password: start-sniffing!

if you don't know wireshark this might be confusing as it might seem that you need to enter these credentials somewhere.
But you cant. This is a hint to fire up wireshark and start sniffing the packets you get when asking to display the satellite data

so open wireshark as sudo (it wont work properly otherwise)
and start sniffing the internet interface you using (in my case i am on my wifi so this is wlan0, if you would be using an ethernet cable this would be using eth0)
restart the init_sat and display the data again

shutting down your browser windows might help in reducing the noise if you are not used to looking at packet traffic.
You should find a group of packets being send to and from the program.
In the bottom hex preview field you should find a packet where the right side contains "CTF" as text.
To more easily read the test rightclick the packet go to follow and click TCP stream. This wil open a box with more easily readable text and all transactions that occured between you and the ip that is sending the data to the init_sat program. Here you can easily read the flag
