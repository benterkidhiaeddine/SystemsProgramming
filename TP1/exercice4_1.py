import os, sys, time
from utils import fork_with_exception_handling, print_pid_ppid


print_pid_ppid()

for i in range(2):
    pid_fils = fork_with_exception_handling()
    if pid_fils == 0:
        print("Je suis le fils ", i + 2)
        print_pid_ppid(2)
        sys.exit(0)

    os.waitpid(pid_fils, 0)


pid_fils = fork_with_exception_handling()
if pid_fils == 0:  # premier fils
    print("Je suis le fils : 1")
    print_pid_ppid(2)
    for i in range(2):
        pid_petit_fils = fork_with_exception_handling()
        if pid_petit_fils == 0:
            print_pid_ppid(3)
            sys.exit(0)
    sys.exit(0)

os.waitpid(pid_fils, 0)
# laisse le deuxième fils affiche son message avant le premier et le troisième

exit(0)
