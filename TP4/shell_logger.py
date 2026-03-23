# un shell ultra basique
import os, sys


if len(sys.argv) == 2:
    sfd = os.open(sys.argv[1], os.O_RDONLY | os.O_CREAT)
    os.dup2(sfd, 0)


while True:
    try:
        cmd = input("")
    except EOFError:
        break
    if cmd == "exit":
        break
    args = cmd.split(" ")
    if os.fork() == 0:

        # Faire la redirection
        fd = os.open("log.txt", os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o644)
        os.dup2(fd, 1)
        os.close(fd)

        os.execvp(args[0], args)
    os.wait()
