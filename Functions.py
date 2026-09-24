# function ---- A block of reusable code place () after the function name to invoke it
# return ---- statement used to end a function and send a result back to the caller 

def display_invoice(username, amount, due_date):
    print(f"Hello {username}!")
    print(f"Your bill of ${amount:.2f} is due : {due_date}")

display_invoice("Shravya", 35.9452, "01/11/2026")

# adding return statement

def add(a, b):
    z = a + b
    return z

def substract(a, b):
    z = a - b
    return z

def multiply(a, b):
    z = a * b
    return z

def divide(a, b):
    z = a / b
    return z

print(add(3, 8))
print(substract(24, 8))
print(multiply(6, 7))
print(divide(64, 8))

