# Tutorial for the code "letterCounter.py" with GUI (user interface)

I recommend doing the CLI tutorial beforehand.
[CLI-Tutorial](https://github.com/Satisfraction/Python-Lernen/tree/main/mini-projekte/Buchstaben%20Z%C3%A4hler%20-%20Letter%20Counter/Letter%20Counter%20(Englisch)/CLI-Tutorial%20(easy))

## Step 1:

- Open your favorite text editor or integrated development environment (IDE) and create a new file named "letterCounter.py" or use the template.

## Step 2:

- Add the following lines of code:

    ```python 
    # Imports 
    import tkinter as tk 
    from tkinter import messagebox.

These lines import the Tkinter module, which is used to create the graphical user interface (GUI), and the `messagebox` class, which is used to display messages.

## Step 3: 

- Add the following lines of code:

    ```python
    # function to calculate the number and percentage value of the letter
    def calculate_percentage():
        user_message = message_entry.get("1.0", tk.END).strip()
        user_letter = letter_entry.get()

        count = user_message.count(user_letter)
        percentage = count / len(user_message) * 100

        messagebox.showinfo("Result", f "The letter {user_letter} occurred {count} times in the message.\n\nThe percentage of occurrences of the letter {user_letter} in the message is {percentage:.2f}%.")

This function `calculate_percentage()` is called when the user clicks on the "Calculate" button. It retrieves the entered text from the `message_entry` message field, removes unnecessary spaces and stores it in the `user_message` variable. The entered letter is retrieved from the `letter_entry` letter field and stored in the `user_letter` variable.

The number of occurrences of the letter in the message is determined using the `count()` method and stored in the `count` variable. The percentage is calculated by dividing the number of occurrences by the total length of the message and multiplying by 100. The result is stored in the `percentage` variable.

Finally, a message is displayed with the results using the `showinfo()` method of the `messagebox` class. The message contains the number of occurrences and the percentage.

## Step 4: 

- Add the following lines of code:

    ```python
    # Creation the GUI window
    window = tk.Tk()
    window.title("Letter counter")
    window.geometry("400x300")

These lines create a window for the GUI application with the title "Letter Counter" and a size of 400x300 pixels.

## Step 5: 

- Add the following lines of code:

    ```python
    # Create the textfields and label
    message_label = tk.Label(window, text="Message:")
    message_label.pack()
    message_entry = tk.Text(window, width=50, height=10)
    message_entry.pack()

    letter_label = tk.Label(window, text="Letter:")
    letter_label.pack()
    letter_entry = tk.Entry(window)
    letter_entry.pack()

These lines create labels and entry fields (text field and single field) for the message and letter in the GUI. The `Label` class is used to create text labels, while the `Text` and `Entry` classes allow input fields for multiline text and a single text, respectively.

## Step 6: 

- Add the following lines of code:

    ```python
    # Create the calculate button
    calculate_button = tk.Button(window, text="Calculate", command=calculate_percentage)
    calculate_button.pack()

These lines create a button with the text "Calculate" in the GUI. When the button is clicked, the function `calculate_percentage()` is called.

## Step 7: 

- Add the following line of code:

    ```python
    # Start the GUI main loop
    window.mainloop()

This line starts the main loop of the GUI application and allows interaction with the user.

## Step 8: 

- Save the file.

## Step 9: 

- Open your command line or terminal and navigate to the location of the "letterCounter.py" file.

## Step 10: 

- Run the code by typing the command `python letterCounter.py` in the command line or terminal.

## Step 11: 

- The GUI window of the application will open.

## Step 12: 

- Type a message in the message box and enter the letter to search for.

## Step 13: 

- Click on the "Calculate" button.

## Step 14: 

- A message box will be displayed showing the results. It shows the number of occurrences of the letter in the message and the calculated percentage.

## Step 15: 

- Click "OK" or close the message box to continue.

Congratulations! You have successfully created and executed the "letterCounter.py" code. This application allows users to count the number of occurrences of a particular letter in a message and display the percentage of occurrences in a simple GUI.

Feel free to try extending the code and adding new features. Have fun trying it out.