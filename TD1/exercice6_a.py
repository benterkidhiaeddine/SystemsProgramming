import os
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} nombre_fils")
        sys.exit(1)

    n = int(sys.argv[1])

    print(f"pid = {os.getpid()}")
    for i in range(1, n + 1):
        try:
            fork_result = os.fork()
        except OSError:
            print("An error occured with forking")
            sys.exit(1)
        if fork_result == 0:
            print(f"pid = {os.getpid()}, fils = {i}")
            sys.exit(0)

        os.wait()

    sys.exit(0)
