import os, sys

fd_r = os.open("front2back.fifo", os.O_RDONLY)
fd_w = os.open("back2front.fifo", os.O_WRONLY)
print("Tube ouvert en lecture")
MAXBYTES = 1024
while True:
    cmd = os.read(fd_r, MAXBYTES)

    if not cmd:
        break
    os.system(cmd.decode())
    os.write(fd_w ,b"ack")
