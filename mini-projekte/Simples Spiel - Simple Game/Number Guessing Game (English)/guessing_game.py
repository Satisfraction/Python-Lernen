# Fill in the gaps according to the instruction in README.md

import   # Import the random module

def play_game():  # Define a function named play_game
      # Print a welcome message
      # Print a message about the range of the secret number
      # Print a message about the number of attempts

      # Generate a random number between 1 and 100 and assign it to secret_number
      # Initialize the attempts counter to 0

    while   # Start a loop that runs as long as attempts is less than 5
          # Prompt the user to enter a guess and convert it to an integer
        attempts += 1  # Increment the attempts counter by 1

        if   # Check if the guess is less than the secret number
              # Print a message indicating that the guess is too low
        elif   # Check if the guess is greater than the secret number
              # Print a message indicating that the guess is too high
        else:  # If neither of the above conditions are true, the guess must be correct
              # Print a message indicating that the guess is correct
            return  # Exit the function
        
    if attempts == 5:
          # If the loop completes without finding the correct number, print a message indicating that the attempts are exhausted
          # Print the value of the secret number

()  # Call the play_game function to start the game
