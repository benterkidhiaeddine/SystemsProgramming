#!/usr/bin/env python3

import errno, os, sys


nbChildren = 20
pid_list = []
for i in range(nbChildren):
    pid = os.fork()
    pid_list.append(pid)
    if pid == 0:  # child
        sys.exit(100 + i)

for pid in pid_list:
    pid, status = os.waitpid(pid, 0)
    if os.WIFEXITED(status):
        print(f"Le processus avec pid {pid} a terminé normalment ")
sys.exit(0)
