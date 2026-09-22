# if -- do some code only IF some condition is true ELSE do something else

age = int(input("Enter your age : "))

if age >= 100:
    print("You are too old to drive")
elif age >= 18:
    print("You are a major and can have Driving License")
elif age < 0:
    print("You haven't born yet!")
elif age < 18:
    print("You are a minor and cannot have Driving License")
else:
    print("You should be 18+ to have Driving License")

#Example 2

online = True

if online:
    print("You are online")
else:
    print("You are offline")