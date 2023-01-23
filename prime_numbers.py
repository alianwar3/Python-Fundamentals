# Check if n is divisible by 1 or itself
for n in range(2, 10):
    for x in range(2, n):

        # If n is divisible by x, means its not a prime number
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

    else:
        print(f"{n} is a prime number.")