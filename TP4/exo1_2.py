import os

octets = os.read(0, 100)
os.write(1, octets)
os.write(2, (f"{len(octets)} octets recopiés stdin->stdout\nbye\n").encode("utf-8"))
