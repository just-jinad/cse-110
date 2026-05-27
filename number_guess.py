import random

keep_playing = "yes"

while keep_playing == "yes":
    secret_number = random.randint(1, 100)
    print(f"{secret_number}")
    user_guess = int(input("Guess a number between 1 and 100: "))

    while user_guess != secret_number:
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        user_guess = int(input("Guess a number between 1 and 100: "))

 
    print("Congratulations! You guessed the number!")

    keep_playing = input("Do you want to play again? (yes/no): ").lower() 