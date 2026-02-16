#!/usr/bin/env python3

import os, sys
from utils import fork_with_exception_handling

fork_result = fork_with_exception_handling()
if fork_result == 0:
    if len(sys.argv) % 2 != 0:
        print("Usage ./lanceur ./afficheur VAR1 VALUE1 ...")
    cmd = sys.argv[1]
    args = sys.argv[1:]
    os.execve(cmd, args)


sys.exit(0)
