cars = [
    {"make": "Ford","model": "Fiesta","mileage": 23000,"fuel_consumed": 460},
    {"make": "Ford","model": "Focus","mileage": 17000,"fuel_consumed": 350},
    {"make": "Mazda","model": "MX-5","mileage": 49000,"fuel_consumed": 900},
    {"make": "Mini","model": "Cooper","mileage": 31000,"fuel_consumed": 235}
]


# Calculate mpg
def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg # As soon as a function returns something, the rest of the code will not execute


# Determine car make and model
def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


# Print car information
def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)

    return f"{name} does {mpg} miles per gallon."


for car in cars:
    print(print_car_info(car))


# divide
def divide(x, y):
    if y == 0:
        return "You tried to divide by zero"
    else:
        return x / y

divide_result = divide(15, 5)
print(divide_result)


# Default parameters
def add(x, y = 3):
    total = x + y
    return total

print(add(5))

# String arguments
print(1, 2, 3, 4, 5, sep=" + ")
