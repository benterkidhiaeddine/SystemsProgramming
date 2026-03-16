import os, sys

fd_w = os.open("front2back.fifo", os.O_WRONLY)
fd_r = os.open("back2front.fifo", os.O_RDONLY)
print("Tube ouvert en écriture")


MAXBYTES = 1024
while True:  # Lit dans l'entrée standard et recopie dans le tube
    print("> ", end="", flush=True)
    cmd = os.read(0, MAXBYTES)
    os.write(fd_w, cmd)
    os.read(fd_r, MAXBYTES)

