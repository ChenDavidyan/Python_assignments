import random


def get_new_guess(cnt):
    guess = input("please write your guess")
    cnt += 1
    return guess, cnt


def offer_new_game():
    if input("would you like to play again? (y/n)").lower() == "y":
        main()


def is_spacial_char(guess, answer, cnt):
    match guess.lower():
        case "x":
            return guess, answer, cnt, "break_loop"
        case "n":
            offer_new_game()
            return guess, answer, cnt, "break_loop"
        case "s":
            cnt -= 1
            print(f"The right answer is {answer}")
            guess, cnt = get_new_guess(cnt)
            return guess, answer, cnt, "continue"
    return guess, answer, cnt, "continue"

def compare_guess_to_answer(guess, answer, cnt):
            if int(guess) == answer:
                print("You are right!")
                print(f"Number of guesses: {cnt} ")
                offer_new_game()
                return guess, answer, cnt, "break_loop"
            if int(guess) > answer:
                print("Try again! Hint: your guess was too big")
            if int(guess) < answer:
                print("Try again! Hint: your guess was too small")
            guess, cnt = get_new_guess(cnt)
            return guess, answer, cnt, "continue"

def invalid_input (cnt):
    cnt -= 1
    print("Invalid input. Try again")
    return cnt


def main():
    answer = random.randrange(1, 21)
    guess, cnt = get_new_guess(0)

    while True:
        guess, answer, cnt, desicion = is_spacial_char(guess, answer, cnt)
        if desicion == "break_loop":
            break
        try:
            guess, answer, cnt, desicion = compare_guess_to_answer(guess, answer, cnt)
            if desicion == "break_loop":
                break   
        except ValueError:
            cnt = invalid_input(cnt)
            guess, cnt = get_new_guess(cnt)


main()
