The STOP GAN challenge was the first pwn challenge.<br />
As last year there were a lot of pwn challenges and I found these quite difficult as I had little experience with it I struggled but learned alot about them. I was thus prepared this year and had been practicing for these challenges a bit in the hope to not be as lost in solving them. <br />
The pwn challenges this year however where a lot more basic than last year.

In this challenge just getting the program to crash got you one flag. This is very easy. Just type enough A's or whatever character you want and if you got enough of them you will get the first flag.

The second flag was a little bit more dificult.<br />
Here we want to controll the crash. The reason the program crashes when entering a lot of characters is that in the code a buffer (a specific amount of memory) is allocated for the string you are about to enter. Nor the code calling the function nor the function used to store your input text itselve checks if the buffer it will write to is smaller than what you put in. So when you write more characters than can be stored in the buffer the excess characters are writing in parts of mememory outside of the buffer. When the code somewhere returns what is in the buffer it will thus not contain these characters.<br />
What is worse is that these excess characters will overwrite parts of memory used for other functionality of the program. This is what is causing the program to crash as this memory now contains giberish for what it should be doing in normal circumstances.

The memory where the buffer is reserving a part of is called the stack. The stack is a block of memory that can be used by the program to store al kinds of different information like buffers containing data but also pointers. <br />
A pointer is a part of memory that contains the adress of some other part of memory. I imagine it like a letterbox containing a note with the adress of another letterbox where you can accualy find your mail. <br />
When a program starts a function call the first thing it does is put the address of the next step after the function in the stack. This way it keeps track of where to go back to after it is done executing the functions code. <br />
In this challenge when you are asked to enter text this is happening in the main function. When the program creates the buffer for your text this is stored right after the pointer of where to go when the main function is done. By filling up the buffer and then writing data that is a valid adress we can now make the program think that when main is done it should go and execute a part that is accualy not correct.

This above is a layman explanation of what is happening. There are added complexities that I have avoided. Pwn challenges are a lot of fun and there are a lot more difficult ways to make code do things it should not. If you are interested you should get yourself familiar whith how the stack works, how pointers work and what kind of countermeasures exist so you can not abuse bugs as easily. For a very good tutorial for learning how to solve pwn challenges I highly recomend the protostar challenges and the explanation videos made by Lifeoverflow. They are very beginner friendly and just plain awesome:<br />
https://old.liveoverflow.com/binary_hacking/protostar/index.html


The exploit code i used can be found here in the bof_pwntool.py file.

I recomend not using a dissasembler for most pwn challenges if you are realy new to this. A dissasembler makes life more easy but you will learn more and be less confused by just starting from the basics. The basic idea of this challenge is already discused in the 3rd video of the lifeoverflow series linked above. However as I did not have the source code of bof here so I did not even know the function that would give me the flag let alone its adress. Even after knowing what to look for with from having used a disassembler I struggled to find the same info just using gdb. I'm not sure if this is due to it being MIPS or just me being to lazy and not looking hard enough (I'm guessing 20%/80% respectively)

So to solve this I first disassembled the code with ghidra. as I need to figure out where to redirect to to get the second flag.
The first thing i do is check the function calls in main. I see in the assembly that at the start there is a call to write_out.<br />
I dont see this call in the dissasembler output? When following what write_out does I see the segfoult message we got from the basic overflow so I am guessing this is not in the dissasembly output as segfaulting is not part of the normal program flow. The write_out function then calls the print_file function with argument flag0. I then looked if this print_file is used elsewhere.<br />
It is. It is used in a function called local_flag where it prints the content of flag1.
So I need to make the controlled crash return to local_flag, the adress of which is 0x00400840.
I thus need to fill the buffer: 260 chars (/bytes) and overwrite the base_pointer 4 chars (/bytes) and then add the adress of local_flag. The pwn library gives some functions to make life more easy like the p32 packing function. The default mode of this function will return me the little endian (reverse order) bytes for this adress to put as the main return adress.

That's all info needed to make the exploit code. running this code prints out both flags!


