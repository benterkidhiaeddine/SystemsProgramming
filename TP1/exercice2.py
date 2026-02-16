import os 


def print_key_value_env():
    for k, v in os.environ.items():
        print(f"VAR: {k} : VALUE {v}")
    


if __name__ == "__main__":
    print_key_value_env() 
    print(len(os.environ.items()))