print("Welcome to the first mini project! I am an application that takes a message and a letter from you. My task is to count how many times this letter occured and to calculate it´s percentage.")

# Get the user inputs
user_message = input("Please enter your message: ")
user_letter = input("Please enter your letter: ")
print(user_message)
print(user_letter)

# Count the number of occurences of the letter in the message
count = user_message.count(user_letter)

# Calculate the percentage of occurences of the letter in the message
percentage = count / len(user_message) * 100

# Print the results
print("The letter", user_letter, "occured", count, "times in the message.")
print("The percentage of occurences of the letter", user_letter, "in the message is", percentage, "%.")