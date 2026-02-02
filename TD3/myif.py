#! /usr/bin/env python3
import os , sys


try:
    idx_then = sys.argv.index("--then")
    idx_else = sys.argv.index("--else")
    idx_fi = sys.argv.index("--fi")
    assert (idx_then <  idx_else < idx_fi == len(sys.argv) - 1)

    args1 = sys.argv[1: idx_then]
    args2 = sys.argv[idx_then + 1: idx_else]
    args3 = sys.argv[idx_else + 1: idx_fi]
    cmd1 = args1[0]
    cmd2 = args2[0]
    cmd3 = args3[0]

except (ValueError, AssertionError, IndexError):
    print("Usage : ./myif.py cmd1 args ...--then cmd2 args ...[ --else cmd3 args ...] --fi ")
    sys.exit(1)


def protected_fork():
    try:
        fork_result = os.fork()
    except OSError as e:
        print(f"Erreur lors du fork : {e}")
        sys.exit(1)
    return fork_result

def protected_exec(cmd, args):
    try:
        os.execvp(cmd, args)
    except (PermissionError, FileNotFoundError) as e:
        print(f"Une erreur est survenue lors de l'éxecution de la commande {cmd}: {e}")
        sys.exit(1)

# Create child process to 
if protected_fork() == 0:
    protected_exec(cmd1 , args1)

try:
    pid , status = os.wait()
except OSError:
    print(f"Une erreur est survenue lors du wait")
    sys.exit(1)

if not os.WIFEXITED(status):
    print("La commande s'est terminé avant de pouvoir donner un code de sorite")
    sys.exit(1)
elif os.WEXITSTATUS(status) == 0:
    if protected_fork() == 0:
        protected_exec(cmd2, args2)
else:
    if protected_fork() == 0:
        protected_exec(cmd3, args3)


try:
    pid , status = os.wait()
    if os.WIFEXITED(status):
        print(f"La commande avec le pid :{pid} a réussi d'étre executé sons statut est {os.WEXITSTATUS(status)}")
    else:
        print(f"La commande avec le pid :{pid} a échoué d'étre executé sons statut est {os.WEXITSTATUS(status)}")

except OSError:
    print(f"Une erreur est survenue lors du wait")
    sys.exit(1)


