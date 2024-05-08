import random


def offer_new_game():
    choice = input("would you like to play again? (y/n)").lower()
    while True:
        if choice == "y":
            return "new_game"
        elif choice == "n":
            return "exit_game"
        else:
            choice = input("Invalid input! would you like to play again? (y/n)")


def is_spacial_char(guess, answer):
    match guess.lower():
        case "x":
            return "exit_game"
        case "n":
            desicion = offer_new_game()
            return desicion
        case "s":
            print(f"The right answer is {answer}")
            return "new_guess"
    return "continue"


def compare_guess_to_answer(guess, answer, cnt):
    if int(guess) == answer:
        print("You are right!")
        print(f"Number of guesses: {cnt} ")
        decision = offer_new_game()
        return decision
    elif int(guess) > answer:
        print("Try again! Hint: your guess was too big")
        return "new_guess"
    elif int(guess) < answer:
        print("Try again! Hint: your guess was too small")
        return "new_guess"


def main():
    while True:
        answer = random.randrange(1, 21)
        cnt = 1

        while True:
            guess = input("please write your guess")
            desicion = is_spacial_char(guess, answer)
            if desicion == "new_game" or desicion == "exit_game":
                break
            elif desicion == "new_guess":
                continue

            try:
                desicion = compare_guess_to_answer(guess, answer, cnt)
                if desicion == "new_game" or desicion == "exit_game":
                    break
            except ValueError:
                print("Invalid input!")
                continue
            cnt += 1

        if desicion == "exit_game":
            break


main()
