"""
Écrire un programme Python qui change de PID toutes les 2 secondes, et affiche à
chaque fois celui-ci.
Note : time.sleep(n) endort un processus pendant n secondes. n est de type float.

"""

import os
import sys
import time

if __name__ == "__main__":
    while True:
        print(f"pid = {os.getpid()}")
        pid = os.fork()
        if pid != 0:
            sys.exit(0)

        time.sleep(2)
