import random

def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 50, 10
    elif choice == "2":
        return 100, 7
    elif choice == "3":
        return 200, 5
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 100, 7


def play_game():
    max_number, attempts = choose_difficulty()
    secret_number = random.randint(1, max_number)

    print(f"\nI have chosen a number between 1 and {max_number}.")
    print(f"You have {attempts} attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess == secret_number:
                print("🎉 Correct! You guessed the number!")
                return
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")

            attempts -= 1
            print("Attempts left:", attempts)

        except ValueError:
            print("Please enter a valid number.")

    print("\n❌ You ran out of attempts.")
    print("The number was:", secret_number)


def main():
    while True:
        play_game()
        again = input("\nPlay again? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for playing!")
            break


main()
