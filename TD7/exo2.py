import os, sys

fd = os.open("hello.txt", os.O_WRONLY | os.O_CREAT, 0o644)

os.dup2(fd, 1)  # rederige la sortie standard '1' vers le fichiher hello.txt
# Comment on a fait cette redirection , tout les ecritures dans la sortie standard '1'
# viont etre rederigé vers le fichier "hello.txt"
print("hello world")

os.write(1, b"Hello world")
