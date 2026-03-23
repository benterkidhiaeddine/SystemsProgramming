import os, sys


if os.fork() == 0:
    fd_r = os.open("father2son.fifo", os.O_RDONLY)
    buf = os.read(fd_r, 1024)
    print("Le fils a lu : ", buf.decode())
    sys.exit(0)
else:
    fd_w = os.open("father2son.fifo", os.O_WRONLY)
    os.write(fd_w, b"Hello, fils!")
    os.wait()
