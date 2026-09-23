# PYTHON DICE ROLLER PROGRAM

import random

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {
    1 : ("┌─────────┐", 
         "│         │", 
         "│    ●    │", 
         "│         │", 
         "└─────────┘"),
    2 : ("┌─────────┐", 
         "│  ●      │", 
         "│         │", 
         "│      ●  │", 
         "└─────────┘"),
    3 : ("┌─────────┐", 
         "│    ●    │", 
         "│    ●    │", 
         "│    ●    │", 
         "└─────────┘"),
    4 : ("┌─────────┐", 
         "│  ●   ●  │", 
         "│         │", 
         "│  ●   ●  │", 
         "└─────────┘"),
    5 : ("┌─────────┐", 
         "│ ●     ● │", 
         "│    ●    │", 
         "│ ●     ● │", 
         "└─────────┘"),
    6 : ("┌─────────┐", 
         "│ ●    ●  │", 
         "│ ●    ●  │", 
         "│ ●    ●  │", 
         "└─────────┘")
}

dice = []
total = 0
num_dice = int(input("How many dice? : "))

for die in range(num_dice):
    dice.append(random.randint(1, 6))

for die in range(num_dice):
    for line in dice_art.get(dice[die]):
        print(line)

for die in dice:
    total += die
print(f"Total is : {total}")


