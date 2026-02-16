import os, sys
from utils import fork_with_exception_handling, print_pid_ppid


print_pid_ppid()
pid_fils = fork_with_exception_handling()
if pid_fils == 0:  # premier fils
    print_pid_ppid(2)
    for i in range(2):
        pid_petit_fils = fork_with_exception_handling()
        if pid_petit_fils == 0:
            print_pid_ppid(3)
            sys.exit(0)

    sys.exit(0)


for i in range(2):
    pid_fils = fork_with_exception_handling()
    if pid_fils == 0:
        print_pid_ppid(2)
        sys.exit(0)


exit(0)
