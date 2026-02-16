import os, sys
from utils import fork_with_exception_handling, print_pid_ppid


def chaine_processus(n):
    for i in range(n):
        fork_result = fork_with_exception_handling()
        if fork_result == 0:  # child
            print_pid_ppid(2)
            exit(0)


if __name__ == "__main__":
    l = len(sys.argv)
    if l != 2:
        print(f"Usage exercice4_a number[0-N]")
        exit(1)
    n = sys.argv[1]

    if not str.isnumeric(n):
        print(f"Usage exercice4_a number[0-N]")
        exit(2)

    n = int(n)

    print_pid_ppid()
    chaine_processus(n)
    exit(0)
