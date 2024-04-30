import random

random_number = random.randrange(1,21)
guesses_cnt = 0
true_guess = False
while not true_guess:
    new_guess = int(input("please write your guess"))
    guesses_cnt += 1
    true_guess = random_number == new_guess
    if true_guess:
        print("You are right!")
        print(f"Number of guesses: {guesses_cnt} ")
        break
    if new_guess > random_number:
        print("Try again! Hint: your guess was too big")
    if new_guess < random_number:
        print("Try again! Hint: your guess was too small")