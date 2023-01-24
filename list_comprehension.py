# friends_ages = [22, 31, 35, 37]
# age_strings = [f"My friend is {age} years old." for age in friends_ages]
# print(age_strings)

# names = ["Rolf", "Bob", "Jen"]
# names_lower = [name.lower() for name in names]
# friend = input("Enter your friend name: ")

# if friend.lower() in names_lower:
#     print(f"{friend} is one of your friends.")


# List comprehension with conditionals
ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]


friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]
present_friends = [
    name for name in guests if name.lower() in friends_lower
]
print(present_friends)

texts = ['a', 'b', 'c', 'd', 'e', 'f']
more_texts = ['a', 'b', 'd', 'e', 'f']

output =  [text for text in texts if text in more_texts]
output2 = [text for text in more_texts if text in texts]