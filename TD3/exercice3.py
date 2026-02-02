#! /usr/bin/env python3
import os , sys

cmd1 = "who"
args1 = ["who"]

cmd2 = "pwd"
args2 = ["pwd"]

cmd3 = "ls"
args3 = ["ls", "-l"]

def execute_cmd_and_wait(cmd, args):
    try:
        fork_res = os.fork()
    except OSError as e:
        print(f"Une erreur est survenue lors du fork : {e}")

    if fork_res == 0:  
        try:
            os.execvp(cmd, args)
        except OSError as e:
            print(f"Une erreur est survenue lors de l'éxecution du process {cmd} {args} : erreur:  {e}")
            sys.exit(1)
    try: 
        os.wait()
    except OSError:
        print("Il y a aucun processu à attendre") 

# Create child process to execute
execute_cmd_and_wait(cmd1, args1)
execute_cmd_and_wait(cmd2, args2)
execute_cmd_and_wait(cmd3, args3)
