import os, sys
x = 1
try:
    pid = os.fork()
except OSError as e:
    print(f"There was a en error trying to fork ,{e}")
    exit(1)
    
if pid == 0: # child
    x = x + 1
    print("child: x =", x)
    sys.exit(0)
# parent
x = x - 1
print("parent: x =", x)
sys.exit(0)


# L'affichahge de ce programme
"""
    child: x = 2    
    paren: x = 0
"""