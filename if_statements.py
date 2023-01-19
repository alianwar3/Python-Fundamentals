friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]
user_name = input("Enter your name: ")

# If user_name enters is in friends
if user_name in friends:
    print("Hello, friend!")

# If user_name enters is in family
elif user_name in family:
    print("Hello, family!")

# If neither is true =
else:
    print("Hello, stranger!")