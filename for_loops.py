# For loops is used to repeat things a defined n of times
friends = ["Rolf", "Jen", "Anne"]

# friend defines each value in friends list
for friend in friends:
    print(friend)


# Start at position 2, till number 20, and skip every 3 numbers
for index in range(2, 20, 3):
    print(index)


students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80}
]


for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}")