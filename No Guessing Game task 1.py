import random

def number_guessing_game():
    # Set the range for the random number
    min_number = 1
    max_number = 100
    
    # Set the maximum number of attempts
    max_attempts = 10
    
    # Generate a random number for the user to guess
    secret_number = random.randint(min_number, max_number)
    
    print("Welcome to the world of Number Guessing Game challenge!")
    print(f"I have selected a number between {min_number} and {max_number}. Can you guess it?")
    
    for attempt in range(1, max_attempts + 1):
        try:
            # Get the user's guess
            user_guess = int(input(f"Attempt {attempt}/{max_attempts}: Enter your guess: "))
            
            # Check if the guess is correct
            if user_guess == secret_number:
                print(f"WOW, Congratulations! You guessed the correct number ({secret_number}) in {attempt} attempts.")
                break
            elif user_guess < secret_number:
                print("OMG Too low! Let's Try again.")
            else:
                print("OMG Too high! Let's Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# Run the game
number_guessing_game()

