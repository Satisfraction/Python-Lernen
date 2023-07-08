# `calculator.py` Tutorial GUI version

## Step 1: 

- Open your favorite text editor or integrated development environment (IDE).

## Step 2: 

- Create a new file and save it as `calculator.py` or use the template.

## Step 3: 

- Paste the following code into the `calculator.py` file:

    ```python
    # Imports
    import tkinter as tk

    # Create a new window
    window = tk.Tk()
    window.title("Simple calculator")
    window.geometry("400x300")


### Explanation:

- The first lines import the Tkinter module used to create the graphical user interface (GUI).
- The next lines create a new window (`window`), set the window title to "Simple Calculator" and the window size to 400x300 pixels.

## Step 4: 

- Add the following code:

    ```python
    # function to perform the addition
    def add():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 + num2
        result_label.config(text=f "The sum of {num1} and {num2} is {result}")

    # function to perform a subtraction
    def subtract():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 - num2
        result_label.config(text=f "The difference between {num1} and {num2} is {result}")

    # function to perform the multiplication
    def multiply():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        result_label.config(text=f "The multiplicate of {num1} and {num2} is {result}")

    # function to perform the division
    def divide():
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        if num2 != 0:
            result = num1 / num2
            result_label.config(text=f "Dividing {num1} by {num2} is {result}")
        else:
            result_label.config(text="Error: division by zero")


### Explanation:

- These lines define four functions (`add`, `subtract`, `multiply` and `divide`), each of which performs a specific mathematical operation.
- Each function reads the input numbers (`num1` and `num2`) from the input fields (`num1_entry` and `num2_entry`) and performs the corresponding operation.
- The result is stored in the variable `result` and written to the text field `result_label` to display it.

## Step 5: 

- Add the following code:

    ```python
    # create entry fields for numbers
    num1_entry = tk.Entry(window)
    num1_entry.pack()

    num2_entry = tk.Entry(window)
    num2_entry.pack()


### Explanation:

- These lines create two entry fields (`num1_entry` and `num2_entry`) where the user can enter the numbers.
- The `entry` class from Tkinter is used to create the input fields.
- The `pack()` method is used to place the input fields in the window (`window`).

## Step 6: 

- Add the following code:

    ```python
    # Create buttons for operations
    add_button = tk.Button(window, text="Add", command=add)
    add_button.pack(padx=5, pady=5)

    subtract_button = tk.Button(window, text="Subtract", command=subtract)
    subtract_button.pack(padx=5, pady=5)

    multiply_button = tk.Button(window, text="Multiply", command=multiply)
    multiply_button.pack(padx=5, pady=5)

    divide_button = tk.Button(window, text="Divide", command=divide)
    divide_button.pack(padx=5, pady=5)


### Explanation:

- These lines create four buttons (`add_button`, `subtract_button`, `multiply_button` and `divide_button`) that allow users to select the appropriate operations.
- Each button has a text (e.g. `add`, `subtract`, etc.) and is associated with the corresponding function (`add`, `subtract`, etc.).
- The `pack()` method is used to place the buttons in the window (`window`).
- The `command` parameters point to the corresponding functions to be executed when the buttons are clicked.

## Step 7: 

- Add the following code:

    ```python
    # Create a label frame for the result.
    result_frame = tk.LabelFrame(window, text="Output", width=300, height=100)
    result_frame.pack(padx=10, pady=10)

    # Create a label for the result
    result_label = tk.Label(result_frame, text="")
    result_label.pack()


### Explanation:

- These lines create a frame (`result_frame`) to display the result and a label field (`result_label`) to contain the result.
- The frame is created with the text `output` and set to a width of 300 pixels and a height of 100 pixels.
- The frame is placed in the window (`window`) using the `pack()` method.
- The label field is created in the frame and left empty for now.

## Step 8:

- Add the following code:

    ```python
    # Start the main event loop
    window.mainloop()


### Explanation:

- This line starts the main event loop of the GUI application.
- The loop runs continuously and allows the user to interact with the application until the window is closed.

## Step 9: 

- Save the file.

## Step 10: 

- Open your command line or terminal and navigate to the location of the 'calculator.py' file.

## Step 11: 

- Run the code by typing the command `python calculator.py` in the command line or terminal.

## Step 12: 

- The GUI window of the calculator will open.

## Step 13: 

- Enter the numbers in the input fields to which the desired operation should be applied.

## Step 14: 

- Click on the appropriate button (Add, Subtract, Multiply or Divide) to perform the operation.

## Step 15: 

- The result will be displayed in the label field.


Congratulations! You have successfully created and executed the `calculator.py` code. This simple calculator program allows the user to select various mathematical operations and apply them to two numbers.