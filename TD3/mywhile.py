#!/usr/bin/env python3

import os
import sys
import time


def protected_fork():
    try:
        pid = os.fork()
    except OSError:
        print("Error during fork")
        sys.exit(1)
    return pid


def protected_execvp(cmd, args):
    try:
        os.execvp(cmd, args)
    except (OSError, PermissionError, FileNotFoundError) as e:
        print(f"Error executing cmd : {cmd} , error {e}")
        sys.exit(1)


try:
    idx_do = sys.argv.index("--do")
    idx_done = sys.argv.index("--done")

    assert idx_do < idx_done == len(sys.argv) - 1

    args1 = sys.argv[1:idx_do]
    args2 = sys.argv[idx_do + 1 : idx_done]
    cmd1 = args1[0]
    cmd2 = args2[0]

except (IndexError, AssertionError, ValueError):
    print(f"Usage {sys.argv[0]} cmd [args ...] --do cmd2 [args ...] --done")
    sys.exit(1)

exit_code_cmd2 = 0
while True:
    if protected_fork() == 0:
        protected_execvp(cmd1, args1)

    # parent
    try:
        pid, status = os.wait()
    except ChildProcessError:
        print("Error waiting for child")
        sys.exit(1)

    if not os.WIFEXITED(status):
        print("The process Ended before the command could run")
        sys.exit(1)

    if os.WEXITSTATUS(status) != 0:
        print(f"Command {cmd1} failed to execute , Exiting...")
        sys.exit(exit_code_cmd2)

    else:  # Command cmd1 was sucessful
        if protected_fork() == 0:
            protected_execvp(cmd2, args2)

        # Parent
        try:
            pid, exit_code_cmd2 = os.wait()
        except ChildProcessError:
            print("Error waiting for child")
            sys.exit(1)

        time.sleep(2)
