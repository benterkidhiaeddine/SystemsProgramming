import os, sys


def fork_with_exception_handling():
    try:
        fork_result = os.fork()
    except OSError as e:
        print("Error : {e}")
        sys.exit(1)
    return fork_result


def print_pid_ppid(rank=1):
    padding = "--" * rank
    print(f"{padding}PID: {os.getpid()}  PARENTPID: {os.getppid()}")
