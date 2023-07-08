# `calculator.py` Tutorial CLI version

## Step 1: 

- Open your favorite text editor or integrated development environment (IDE).

## Step 2: 

- Create a new file and save it as `calculator.py` or use the template.

## Step 3: 

- Paste the following code into the `calculator.py` file:

    ```python
    # This is a simple calculator program.

    # Function to add two numbers
    def add(num1, num2):
        return num1 + num2

    # function to subtract two numbers
    def subtract(num1, num2):
        return num1 - num2

    # function to multiply two numbers
    def multiply(num1, num2):
        return num1 * num2

    # function to divide two numbers, handles division by zero
    def divide(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: division by zero"

    # prints the title of the calculator
    print("Simple calculator")
    print("------------------")


### Explanation:


- The upper part of the code defines four functions: `add`, `subtract`, `multiply` and `divide` to perform addition, subtraction, multiplication and division of numbers.
- Each function takes two arguments (`num1` and `num2`) and returns the result of the corresponding operation.
- The `add` function adds `num1` and `num2`, the `subtract` function subtracts `num2` from `num1`, the `multiply` function multiplies `num1` and `num2`, and the `divide` function divides `num1` by `num2`.
- The `divide` function also contains a condition that checks if `num2` is not equal to 0, to prevent division by zero. If `num2` is 0, the error message "Error: Division by zero" is returned.

## Step 4: 

- Add the following code:

    ```python
    # Start an infinite loop for user interaction
    while True:
        # print the available operations
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. divide")
        print("5. Exit")


### Explanation:

- These lines create an infinite loop that allows user interaction. The code is executed repeatedly until the user exits the program.
- Within the loop, the available operations are displayed on the screen.

## Step 5: 

- Add the following code:

    ```python
        # prompt the user to enter his choice
        choice = input("Enter a choice (1-5): ")


### Explanation:

- This line prompts the user to enter their choice by entering a number from 1 to 5.

## Step 6: 

- Add the following code:

    ```python
        # Check if the user wants to exit
        if choice == '5':
            print("Goodbye!")
            break


### Explanation:

- These lines check if the user has selected the "Exit" option.
- If the user enters '5', the message "Goodbye!" is printed and the loop is ended with `break`.

## Step 7: 

- Add the following code:

    ```python
        # prompt the user to enter the two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))


### Explanation:

- These lines prompt the user to enter the two numbers to which the selected operation should be applied.
- The `float()` function is used to ensure that the values entered are interpreted as floating point numbers.

## Step 8: 

- Add the following code:

    ```python
        # Execute the selected operation based on the user's choice
        if choice == '1':
            result = add(num1, num2)
            print(f "The sum of {num1} and {num2} is {result}")
        elif choice == '2':
            result = subtraction(num1, num2)
            print(f "The difference between {num1} and {num2} is {result}")
        elif choice == '3':
            result = multiplication(num1, num2)
            print(f "The product of {num1} and {num2} is {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f "The division of {num1} by {num2} is {result}")
        else:
            print("Invalid input, please try again.")


### Explanation:

- These lines perform the selected operation based on the user choice.
- The `if-elif-else` statements check the value of the `choice` variable and call the corresponding function (add, subtract, multiply or divide).
- The result of the operation is stored in the `result` variable and printed on the screen together with the input numbers.
- If the user makes an invalid input (no number between 1 and 5), the message "Invalid input. Please try again." is output.

## Step 9: 

- Add the following code:

    ```python
        print("Invalid input. Please try again.")


### Explanation:

- This line prints a message if the user made an invalid input for the options.

## Step 10: 

- Save the file.

## Step 11: 

- Open your command line or terminal and navigate to the location of the `calculator.py` file.

## Step 12: 

- Run the code by typing the command `python calculator.py` in the command line or terminal.

## Step 13: 

- The title line of the calculator `Simple Calculator` will be displayed on the screen.

## Step 14: 

- The program offers a list of available operations and asks the user to make a choice.

## Step 15: 

- Enter a number from 1 to 5 to select the desired operation.

## Step 16: 

- When you enter '5', the program will exit and the message "Goodbye!" will be displayed.

## Step 17: 

- For the other options, the program will prompt the user to enter the two numbers to which the operation should be applied.

## Step 18: 

- The program executes the selected operation and outputs the result on the screen.

## Step 19: 

- The program returns to the menu and again prompts the user to select an operation.


Congratulations! You have successfully created and executed the `calculator.py` code. This simple calculator program allows the user to select various mathematical operations and apply them to two numbers.