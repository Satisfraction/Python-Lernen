# Tutorial for the code "letterCounter.py"

## Step 1: 

Open your favorite text editor or integrated development environment (IDE) to type the code.

## Step 2: 

Create a new file named "letterCounter.py" or use the template. 

- Paste the following code:

    ```python
    # Welcome message
    print("Welcome to the first mini project! I am an application that accepts a message and a letter from you. My job is to count how many times that letter appears in the message and calculate its percentage.")

This code outputs a welcome message to inform the user about the functionality of the application.

## Step 3: 

- Add the following code:

    ```python
    # Retrieve the user input
    user_message = input("Please enter your message: ")
    user_letter = input("Please enter your letter: ")

These two lines prompt the user to enter a message and a letter to be counted in the message. The user's input is stored in the `user_message` and `user_letter` variables.

## Step 4: 

- Add the following code:

    ```python
    # Print the user input
    print(user_message)
    print(user_letter)

These two lines print the entered message and letter on the screen to confirm to the user that the input was captured correctly.

## Step 5: 

- Add the following code:

    ```python
    # Counts the number of occurrences of the letter in the message.
    count = user_message.count(user_letter)

This line uses the `count()` method to get the number of occurrences of the input letter `user_letter` in the input message `user_message`. The result is stored in the `count` variable.

## Step 6: 

- Add the following code:

    ```python
    # Calculate the percentage of occurrence of the letter in the message.
    percentage = count / len(user_message) * 100

This line calculates the percentage of occurrences of the letter in the message. First, the number of occurrences `count` is divided by the total length of the message `len(user_message)`. Then the result is multiplied by 100 to get the percentage. The result is stored in the variable `percentage`.

## Step 7: 

- Add the following code:

    ```python
    # Print the results
    print("The letter", user_letter, "occurs", count, "times in the message.")
    print("The percentage of occurrences of the letter", user_letter, "in the message is", percentage, "%.")

These two lines print the results on the screen. They show the number of occurrences of the letter in the message and the calculated percentage.

## Step 8: 

- Save the file.

## Step 9: 

- Open your command line or terminal and navigate to the location of the "letterCounter.py" file.

## Step 10: 

- Run the code by typing the command `python letterCounter.py` in the command line or terminal.

## Step 11: 

- The application will greet you and ask for your message and letter. 
- Type the appropriate input and press enter.

## Step 12: 

- The application will output the entered message and letter.

## Step 13: 

- The application counts the number of occurrences of the letter in the message and calculates the percentage.

## Step 14: 

- The application outputs the results, including the number of occurrences and the percentage.


Congratulations! You have successfully created and executed the "letterCounter.py" code. This code allows users to count the number of occurrences of a particular letter in a message and calculate the percentage of occurrences.