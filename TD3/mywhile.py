#!/usr/bin/env python3

import os
import sys
import time


def protected_fork():
    try:
        pid = os.fork()
    except OSError as e:
        print(f"Error during fork: {e}", file=sys.stderr)
        sys.exit(1)
    return pid


def protected_execvp(cmd, args):
    try:
        os.execvp(cmd, args)
    except (OSError, PermissionError, FileNotFoundError) as e:
        print(f"Error executing cmd : {cmd} , error {e}", file=sys.stderr)
        sys.exit(1)


# --- Argument Parsing ---
try:
    idx_do = sys.argv.index("--do")
    idx_done = sys.argv.index("--done")

    assert idx_do < idx_done == len(sys.argv) - 1

    args1 = sys.argv[1:idx_do]
    args2 = sys.argv[idx_do + 1 : idx_done]
    cmd1 = args1[0]
    cmd2 = args2[0]

except (IndexError, AssertionError, ValueError):
    print(f"Usage: {sys.argv[0]} cmd1 [args ...] --do cmd2 [args ...] --done")
    sys.exit(1)

# --- Main Loop ---
exit_code_cmd2 = 0

while True:
    # 1. Run the condition command (cmd1)
    if protected_fork() == 0:
        protected_execvp(cmd1, args1)

    # Parent waits for cmd1
    try:
        pid, status1 = os.wait()
    except ChildProcessError:
        print("Error waiting for cmd1 child", file=sys.stderr)
        sys.exit(1)

    if not os.WIFEXITED(status1):
        print(f"The process {cmd1} ended unexpectedly (e.g., via signal).")
        sys.exit(1)

    # If cmd1 fails, break the loop and exit with cmd2's last known exit code
    if os.WEXITSTATUS(status1) != 0:
        print(f"Command {cmd1} failed to execute. Exiting...")
        sys.exit(exit_code_cmd2)

    # 2. cmd1 succeeded! Run the action command (cmd2)
    if protected_fork() == 0:
        protected_execvp(cmd2, args2)

    # Parent waits for cmd2
    try:
        pid, status2 = os.wait()
    except ChildProcessError:
        print("Error waiting for cmd2 child", file=sys.stderr)
        sys.exit(1)

    # Extract the clean exit code for cmd2 safely
    if os.WIFEXITED(status2):
        exit_code_cmd2 = os.WEXITSTATUS(status2)
    else:
        print(f"Command {cmd2} ended unexpectedly.")
        exit_code_cmd2 = 1  # Force a failure code if it was killed

    # 3. Pause before polling again
    time.sleep(2)
