"""
. Écrire un programme Python qui affiche son PID, puis crée un fils. Le père affiche
son PID, attend la terminaison du fils puis affiche son code de sortie.

"""

import os
import sys
import time

if __name__ == "__main__":
    print(f"pid = {os.getpid()}")

    try:
        fork_result = os.fork()
    except OSError:
        print("Probleme with forking")
        sys.exit(1)

    if fork_result == 0:
        print(f"pid = {os.getpid()} child")
        time.sleep(100)
        sys.exit(0)

    pid, status = os.wait()
    print(f"pid = {os.getpid()}")
    if os.WIFEXITED(status):
        print(f"child process ended normally with exit status {os.WEXITSTATUS(status)}")
    else:
        print(f"child process ended abnormally with exit status {os.WTERMSIG(status)}")
    sys.exit(0)
