"""
1. Écrire un programme Python qui affiche son PID, puis crée un fils. Le père affiche
son PID, puis affiche un message signalant que son fils est mort lorsque c’est bien
le cas. Le fils affiche son PID, s’endort 5 secondes puis se termine.

"""

import os
import sys
import time

if __name__ == "__main__":
    print(f"pid = {os.getpid()}")

    try:
        fork_result = os.fork()
    except OSError:
        print("Probleme forking")
        sys.exit()

    if fork_result == 0:
        print(f"pid = {os.getpid()}")
        time.sleep(5)
        sys.exit(0)

    pid, status = os.wait()

    print(f"pid = {os.getpid()}, child process ended")
    sys.exit(0)
