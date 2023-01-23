cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]


for status in cars:
    if status == "faulty":
        print("Stopping the production line!")
        break
    print(f"This car is {status}")
    print("Shipping new car to customer!")

# If the loop completely ran without a break or no errors, else will be printed
else:
    print("All cars built successfully. No faulty cars!")