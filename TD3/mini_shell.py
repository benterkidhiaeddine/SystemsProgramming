#! /usr/bin/env python3
import os , sys

while True:
    print("minishell> ", end="")
    argv = input()
    argv = argv.strip()
    argv = argv.split()
    if len(argv) == 0:
        continue
    cmd = argv[0] 

# Create child process to execute
    if os.fork() == 0:
        try:
            os.execvp(cmd, argv)
        except (OSError ,Exception) as e:
            print(f"une erreur est survenue: {e}" , file=sys.stderr)
            sys.exit(1) 
    else:
        os.wait()

