# Iterables --- An object/collection that can return its elements one at a time, allowing it to be iterated
#                   over in a loop

dict = {"A":1, "B":2, "C":3, "D":4}

for key,value in dict.items():
    print(f"{key} = {value}")

# Membership Operators ---- used to test whether a value or variable is found in a sequence in/not in

word = "PINEAPPLE"

letter = input("Guess a letter in the secret word : ").strip().upper()

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")

