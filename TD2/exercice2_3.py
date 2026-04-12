import os
import sys

print("Hello")
pid = os.fork()
print(f"ici : {pid}")
if pid != 0:
    pid_wait, status = os.waitpid(-1, 0)
    if os.WIFEXITED(status):
        print(f"là : {os.WEXITSTATUS(status)}")
        print("Bye")
    sys.exit(2)
sys.exit(0)
