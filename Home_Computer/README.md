In the Home Computer challenge we get 2 files:
- note.txt
- family.ntfs

The note is there to make the challenge solvable on macOS

the .ntfs file is a windows file systhem that can be mounted.
to do so run:
sudo mount -t ntfs family.ntfs /mnt/ntfs (you might need to make the /mnt/ntfs folder first)

you can now cd into /mnt/ntfs/ and you will see some folders and windowsy files
on close inspection you see that most of there files are empty (ls -hal)
This is probably done so you would not be waisting time looking at irrelevant files. To find any files that are not empty run the folowing command in the /mnt/ntfs folder:
find . -type f -size +1c
(-type f -> look for only files no directoryes, -syze +1c -> any files larger(+) than 1 byte(c))

this will show you there is only one interesting file:
./Users/Family/Documents/credentials.txt

when we read the content we get:
I keep pictures of my credentials in extended attributes.

Ok so some googleing of how to read extended attributes gave me:
getfattr ./Users/Family/Documents/credentials.txt

this will show you thare is indeed one file attribute attached: user.FILE0

to get the content run:
getfattr -n user.FILE0 ./Users/Family/Documents/credentials.txt

This gives you a blob of text. It seems base64 encoded. Googleing also tells me that base64 encoding of images is common.
Howerver after some tries I cant seem to manage to make it show a picture.

A bit later I finaly read the man page for getfattr (the other commands i got from google). 
I should have done this a lot sooner instead of trying to get this base64 thing to work cause when you run:
getfattr --only-values -n user.FILE0 ./Users/Family/Documents/credentials.txt | less
you get a file where the header is showing PNG and it looks a lot more like a normal image file.
so write this to a file:
getfattr --only-values -n user.FILE0 ./Users/Family/Documents/credentials.txt > ~/creds.png
you can now open the image from your filesystem and you will see the flag!

