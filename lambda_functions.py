# Structure of a lamdba function
# 1.) lambda keyword
# 2.) Inputs
# 3.) After colon, return value of function
divide_add = lambda x, y, z: (x / y) + z
print(divide_add(15, 3, 5))


average = lambda grade: sum(grade) / len(grade)
print(average([10, 20, 30]))


# First class functions ->
#   We can assign functions to variables
#   Pass it as arguments to other functions
avg = lambda grade: sum(grade) / len(grade)
total = lambda grade: sum(grade)
top = lambda grade: max(grade)


operations = {
    "average": avg,
    "total": total,
    "top": top
}


students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (58, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)}
]


for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ")

    operation_function = operations[operation]
    print(operation_function(grades))   # Once we have the operation_function inside the operations object, we can pass the student grades (to the specific lambda function)