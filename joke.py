import pyjokes
import time
import random

def tell_random_joke():
    joke = pyjokes.get_joke()
    print(joke)

def main():
    while True:
        tell_random_joke()
        time.sleep(300)  # 5 minutes in seconds

if __name__ == "__main__":
    main()
