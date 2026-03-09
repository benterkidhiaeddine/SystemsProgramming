import os, sys, time, signal


def sigint_flow():
    def handler(sig, ignore):
        print(f"Caught Signal with number {sig}")
        sys.exit(0)

    signal.signal(signal.SIGINT, handler)

    signal.pause()


# Won't work because we can't modify the handling of the sigkill handler
def sigkill_flow():
    def handler(sig, ignore):
        print(f"Caught Signal with number {sig}")
        sys.exit(0)

    signal.signal(signal.SIGKILL, handler)

    signal.pause()


# Won't work becauce we can't modify the handling of the sigstop flow
def sigstop_flow():
    def handler(sig, ignore):
        print(f"Caught Signal with number {sig}")
        sys.exit(0)

    signal.signal(signal.SIGSTOP, handler)

    signal.pause()


if __name__ == "__main__":
    # sigkill_flow()
    # sigstop_flow()
    sigint_flow()
