import random

random_number = random.randrange(1, 21)
guesses_cnt = 0
while True:
    new_guess = int(input("please write your guess"))
    guesses_cnt += 1
    if new_guess == random_number:
        print("You are right!")
        print(f"Number of guesses: {guesses_cnt} ")
        break
    if new_guess > random_number:
        print("Try again! Hint: your guess was too big")
    if new_guess < random_number:
        print("Try again! Hint: your guess was too small")
