# Logical Operators --- evaluate multiple conditions (or, and, not)

temp = -10
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is HOT sunny 🥵")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
elif 30 > temp > 0 and is_sunny:
    print("It is WARM outside 🙂")
elif temp >= 28 or is_sunny:
    print("It is HOT sunny 🥵")
elif temp <= 0 and not is_sunny:
    print("It is Cloudy 🥶")
elif 30 > temp > 0 and is_sunny:
    print("It is WARM outside 🙂")
else:
    print("The temparature is goods")
