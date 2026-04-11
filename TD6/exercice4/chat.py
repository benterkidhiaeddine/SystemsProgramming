import os
import sys

MAXSIZE = 100
if sys.argv[1] == "-r":
    fd_in = os.open(sys.argv[2], os.O_RDONLY)
    fd_out = os.open(sys.argv[3], os.O_WRONLY)
else:
    fd_out = os.open(sys.argv[2], os.O_WRONLY)
    fd_in = os.open(sys.argv[3], os.O_RDONLY)
while True:
    # Read from stdin
    buf = os.read(0, MAXSIZE)

    # If nothing comes close the process
    if len(buf) == 0:
        sys.exit(0)

    # Write to fd_out
    os.write(fd_out, buf)

    # Read what's coming from the other chat
    buf = os.read(fd_in, MAXSIZE)

    # If nothing comes exit
    if len(buf) == 0:
        sys.exit(0)

    # write what came to stdout
    os.write(1, buf)
