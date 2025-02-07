from random import randint


def guessing_game():
    answer = randint(1, 100)
    guess_count = 1

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
        except:
            print("Enter valid number between 0 to 100")
            continue

        if user_guess == answer:
            print(
                f"Awesome! You got it! The number was {answer}, and it only took you {guess_count} tries!")
            break

        if user_guess > answer:
            print("Too high!")

        if user_guess < answer:
            print("Too low!")

        guess_count += 1


if __name__ == "__main__":
    guessing_game()
