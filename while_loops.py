# Loops are used to repeat things n of times
is_learning = True

# This condition will repeat, until is_learning is no longer true
# Use to repeat something an undefined n of times
while is_learning:
    print("You're learning")
    user_name = input("Are you still learning? ")

    is_learning = user_name == "yes"
    print(is_learning)


# This will evaluate to True, and the program will repeat itself
repeat_menu = True

while repeat_menu:
    user_input = input("Select either menu option: p/q ") # Ask for user input

    # If user_input is 'p', print "Hello"
    if user_input == 'p':
        print("Hello")

    # If user_input is 'q', print "Terminate", set repeat_menu to False and end while loop
    if user_input == 'q':
        print("Terminate")
        repeat_menu = False