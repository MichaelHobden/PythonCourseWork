import sys
import random

min_num = int(sys.argv[1])
max_num = int(sys.argv[2])

rnd = random.randint(min_num, max_num)
print(rnd)

while True:
    try:
        guess = input(f"Guess a number between {min_num} and {max_num}: ")
        if min_num <= int(guess) <= max_num:
            if int(guess) == int(rnd):
                print("You are a genius")
                break
            else:
                print("Better luck next time!")
        else:
            print("Number not in range!")
    except ValueError:
        print("Value not a number")
    except TypeError:
        print("Value not a number")

