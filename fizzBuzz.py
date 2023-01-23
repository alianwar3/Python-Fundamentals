# Print out numbers from 1 to 100 (including 100).
# But, instead of printing multiples of 3, print "Fizz"
# Instead of printing multiples of 5, print "Buzz"
# Instead of printing multiples of both 3 and 5, print "FizzBuzz".

def fizzBuzz():

    for n in range(1, 101):

        # If n is multiple of both 3 and 5, print "FizzBuzz"
        if (n % 3 == 0) and (n % 5 == 0):
            print("FizzBuzz")

        # If n is multiple of 3, print "Fizz"
        elif (n % 3 == 0):
            print("Fizz")

        # If n is multiple of 5, print "Buzz"
        elif (n % 5 == 0):
            print("Buzz")

        # Else print n
        else:
            print(n)


if __name__ == '__main__':
    fizzBuzz()