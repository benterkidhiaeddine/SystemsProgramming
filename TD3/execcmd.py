#! /usr/bin/env python3
import os , sys

try:
    filename = sys.argv[1]
    argv = sys.argv[1:]
    os.execv(filename, argv)
except IndexError:
    print(f"Usage: {sys.argv[0]} <command> [args...]")
    sys.exit(1)
except OSError as e:
    print(f"{sys.argv[1] } n'a pas été retrouvé")
    sys.exit(1)
except PermissionError:
    print("Le droit d'execution n'est pas correcte")
    sys.exit(1)