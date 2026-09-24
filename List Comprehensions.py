# List Comprehension --- A concise way to create lists in Python. Compact and easier to read than traditional loops
#                           [expression for value in iterable if condition]

# old method
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

# new method

triple = [x * 3 for x in range(1, 11)]
squares = [y * y for y in range(1, 10)]

print(triple)
print(squares)

# Example

numbers = [1, -6, -7, 2, 8, -9, -4, -2, 3]

pos_nums = [num for num in numbers if num >= 0]
neg_nums = [num for num in numbers if num < 0]
even_num = [num for num in numbers if num % 2 == 0]
odd_num = [num for num in numbers if num % 2 == 1]

print(pos_nums)
print(neg_nums)
print(even_num)
print(odd_num)