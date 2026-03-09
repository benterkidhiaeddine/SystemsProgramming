import os, sys

fd = os.open("toto.txt", os.O_RDONLY)
pid = os.fork()
if pid == 0:
    c = os.read(fd, 1)
    sys.exit(0)
os.wait()
c = os.read(fd, 1)
print(c)
sys.exit(0)
