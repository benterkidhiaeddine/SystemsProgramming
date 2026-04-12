import os
import sys

"""
1. Modifier ce programme pour qu’il affiche les numéro des processus dans l’ordre dans
lequel ils ont été créés.

"""


nbChildren = 20

child_pids = []
for i in range(nbChildren):
    pid = os.fork()
    child_pids.append(pid)
    if pid == 0:  # child
        sys.exit(100 + i)


for child_pid in child_pids:
    pid, status = os.waitpid(child_pid, 0)
    if os.WIFEXITED(status):
        print(
            f"child {pid} terminated normally with exit status={os.WEXITSTATUS(status)}"
        )
    else:
        print(f"child {pid} terminated abnormally")


sys.exit(0)
