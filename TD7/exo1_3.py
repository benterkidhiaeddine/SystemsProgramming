import os, sys

fd1 = os.open("toto.txt", os.O_RDONLY)
fd2 = os.open("toto.txt", os.O_RDONLY)
bytes_sequence = os.read(fd1, 2)  # séquence d'octets
bytes_sequence = os.read(fd2, 6)
os.close(fd1)
os.close(fd2)
print(bytes_sequence)
print(bytes_sequence.decode("utf-8"))
print(bytes_sequence.decode("latin-1"))

sys.exit(0)


# Convertir d'utf-8 en latin-1
def convert_utf8_to_latin1(ch_utf8):
    return ch_utf8.decode("utf-8").encode("latin-1")


# Les charactère accentués dans latin-1 sont encodés sur un octet


assert convert_utf8_to_latin1(b"az\xc3\xa8rt") == b"az\xc3\xa8rt"
