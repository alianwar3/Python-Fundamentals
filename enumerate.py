friends = ["Rolf", "John", "Anna"]


for counter, friend in enumerate(friends, start=1):
    print(counter, friend)


print(list(enumerate(friends)))
print(dict(enumerate(friends)))
