import os, sys
try:
    os.fork()
except OSError as e:
    print(f"Error while executing fork {e}")
    exit(1)
print("hello!")
sys.exit(0)
