import os, sys

fd1 = os.open("toto.txt", os.O_RDONLY)
bytes_sequence = os.read(fd1, 2)  # séquence d'octets
print(bytes_sequence)  # b'az' , le b veut dire que c'est une séquence d'octets
print(bytes_sequence.decode("utf-8"))  # 'az'

bytes_sequence = os.read(fd1, 1)
os.close(fd1)
print(bytes_sequence)  # le `é' est codé sur deux octets b'\xc3' encodage hexadécimal
print(bytes_sequence.decode("utf-8"))
# il y a une erreur parceque justement on est entrain
# de lire qu'un seul octect dans un charactère qui est codé sur deux octets
sys.exit(0)
