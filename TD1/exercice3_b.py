import os, sys

def do_it():
    try:
        os.fork()
        os.fork()
    except OSError as e:
        print(f"Error while runinf fork {e}")
        exit(1)
    print("hello")
if __name__ == "__main__":
    do_it()
    print("hello")
    sys.exit(0)
