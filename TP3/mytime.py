#!/usr/bin/env python3
import os, sys, time, statistics

usage_script = "Usage: mytime.py [-n k] [-s] commande [arg ...]"

args = sys.argv
if len(args) < 2:
    print(usage_script)
    sys.exit(1)

repeat_command = False
show_exit_status = False
command_idx = 1
n = 1

i = 1
while i < len(args):
    if args[i] == "-n" and not repeat_command:
        repeat_command = True
        i += 1
        try:
            n = int(args[i])
            i += 1
            if n <= 0:
                raise ValueError
        except (IndexError, ValueError):
            print(usage_script)
            sys.exit(1)
    elif args[i] == "-s" and not show_exit_status:
        i += 1
        show_exit_status = True
    else:
        break

command = args[i]
command_args = args[i:]

elapsed_times = []

for i in range(1, n + 1):
    start = time.time()  # ① time each run individually

    try:
        pid = os.fork()
    except OSError as e:
        print("Error:", e)
        sys.exit(1)

    if pid == 0:  # Child
        try:
            os.execvp(command, command_args)

        except OSError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)  # ② always exit the child

    # Parent: wait for this child before forking the next
    _, status = os.waitpid(pid, 0)  # ③ wait immediately
    elapsed = time.time() - start

    if show_exit_status:
        print(f"Code de sortie : {os.WEXITSTATUS(status)}")

    seconds = int(elapsed)
    microseconds = int((elapsed - seconds) * 1_000_000)
    print(f"{i}. Durée : {seconds}s {microseconds}µs")
    elapsed_times.append(elapsed)

if n > 1:  # ④ only print mean for multiple runs
    mean = statistics.mean(elapsed_times)
    s, us = int(mean), int((mean - int(mean)) * 1_000_000)
    print(f"\nDurée moyenne : {s}s {us}µs")
