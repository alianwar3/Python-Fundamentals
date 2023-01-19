# Break exits a loop if a certain condition is met
# Continue goes forth with the loop if the condition is met
cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping...")
        continue # break
    print(f"This car is {status}")
    print("Shipping new car to customer!")