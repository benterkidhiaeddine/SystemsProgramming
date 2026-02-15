import os, sys
for i in range(2):
    try:
        os.fork()
    except OSError as e:
        print(f"Error while running fork {e}")
        exit(1)
print("hello!")
sys.exit(0)
