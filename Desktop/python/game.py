import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    print("Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too Low! Try again.")
            elif guess > number_to_guess:
                print("Too High! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Please enter a valid number.")

# Start the game
guess_the_number()
