import os, sys


RW_R_R_PERMISSIONS = 0o644

try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]
    cmd = sys.argv[4]
    args = sys.argv[4:]
except IndexError:
    print("exo_redirection.py <file1> <file2> <file3> cmd [args ...]")
    sys.exit(1)

try:
    pid = os.fork()
except OSError as e:
    print("Error", e)
    sys.exit(1)
if pid == 0:
    fd1 = os.open(file1, os.O_RDONLY)
    fd2 = os.open(file1, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, RW_R_R_PERMISSIONS)
    fd3 = os.open(file1, os.O_WRONLY | os.O_CREAT | os.O_APPEND, RW_R_R_PERMISSIONS)

    os.dup2(fd1, 0)
    os.dup2(fd2, 1)
    os.dup2(fd3, 2)

    # N'oublie de femer les descripteur non utilisables
    os.close(fd1)
    os.close(fd2)
    os.close(fd3)

    try:
        os.execvp(cmd, args)
    except OSError as e:
        print("Error", e)
        sys.exit(1)


pid, status = os.wait()
