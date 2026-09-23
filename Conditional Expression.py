# Conditional Expression -- A one-line shortcut for the if-else statements 

num = 4

a = 17
b = 8

age = int(input("Enter age : "))

result = "EVEN" if num % 2 == 0 else "ODD"

max_num = a if a > b else b
min_num = a if a < b else b

status = "ADULT" if age >= 18 else "CHILD"

print(result)

print(max_num)
print(min_num)

print(status)