import os
import sys
import time

# Create the pipe if it dosen't exist

try:
    os.mkfifo("simple.fifo", 0o644)
except FileExistsError:
    os.write(1, b"The fifo already exist , continue execution\n")

# create variable to store the chunk size to be writtend each time
CHUNK_SIZE = 1024

# create the variable that stores the total size
MAXREAD = 0

# Create a child process that reads from the fifo
try:
    pid = os.fork()
except OSError:
    os.write(1, b"Couldn't create child process \n")
    sys.exit(1)


if pid == 0:  # child
    r_fd = os.open("simple.fifo", os.O_RDONLY)
    # Don't read from the fifo just open and let it be filled

    # Don't close the chilld process too fast or writing will raise a Broken Pipe errro
    time.sleep(5)
    sys.exit(0)
else:
    w_fd = os.open("simple.fifo", os.O_WRONLY)

    # Make sure that writing into the fifo is not blocking this way it will raise an error when trying to write into a filled pipe
    os.set_blocking(w_fd, False)
    while True:
        try:
            # generate a buffer that contains CHUNK_SIZER of Bytes
            bytes_to_write = b"b" * CHUNK_SIZE
            written = os.write(w_fd, bytes_to_write)
            MAXREAD += written

        except BlockingIOError:
            os.write(1, b" The pipe is completly full\n")
            break

        except BrokenPipeError:
            os.write(b"The reader closed the pipe too early\n")
            break

        except OSError as e:
            print(f"Probleme {e}")
            break

    os.waitpid(pid, 0)
os.write(1, b"The size of the pipe is " + str(MAXREAD).encode("utf-8") + b"\n")
sys.exit(0)
