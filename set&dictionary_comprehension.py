# Set comprehension
friends = ["Rolf", "ruth", "charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

print(friends_lower.intersection(guests_lower))


friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]


# Append key/value using for loop
long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
}

print(long_timers)


# Zip function
long_timers2 = dict(zip(friends, time_since_seen))
print(long_timers2)