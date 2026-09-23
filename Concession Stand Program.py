# CONCESSION STAND PROGRAM

menu = {
    "pizza": 3.00,
    "nachos": 5.67,
    "popcorn": 4.32,
    "fries": 2.48,
    "chips": 1.00,
    "pretzel": 4.03,
    "soda": 3.00 }

cart = []
total = 0

print("-------------MENU------------")
for key, value in menu.items():
    print(f"{key} : ${value:.2f}")
print("------------------------------")

while True:
    food = input("Select an item (q for quit) : ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-----------YOUR ORDER------------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print("------------------------------")

print()
print(f"Total is : ${total:.2f}")
