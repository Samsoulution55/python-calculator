import random

def play_game():
    # The cloud computer picks a secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 7
    
    print("=" * 40)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it. Good luck!")
    print("=" * 40)

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")
        
        # Get the player's guess safely
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue
            
        # Check the guess
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the secret number {secret_number} correctly!")
            return
        elif guess < secret_number:
            print("📉 Too low! Try a higher number.")
        else:
            print("📈 Too high! Try a lower number.")
            
        attempts -= 1

    print(f"\nGame Over! You ran out of attempts. The secret number was {secret_number}.")

# Start the game loop
if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes' and play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break