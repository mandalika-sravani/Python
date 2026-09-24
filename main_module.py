# if__ name __ == __main__ : (this script can be imported OR run standalone)
#                             Functions and classes in this module can be reused without the main block of code executing

def fav_food(food):
    print(f"Your favourite food is {food}")

def main():
    fav_food("tomato rice")

if __name__ == '__main__':
    main()