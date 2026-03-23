import os, sys

fd_r, fd_w = (
    os.pipe()
)  # création du pipe et ouverture des descripteurs de fichiers au meme temps

if os.fork() == 0:
    buf = os.read(fd_r, 1024)
    print("Le fils a lu : ", buf.decode())
    sys.exit(0)
else:
    os.write(fd_w, b"Hello, fils!")
    os.wait()
