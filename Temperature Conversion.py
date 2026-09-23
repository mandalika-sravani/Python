# Python Temperature Conversion

unit = input("Fahrenheit or Celsius? (F or C): ")
temp = float(input("Enter the Temperature: "))

if unit == 'F':
   temp = round((temp - 32) * 5 / 9, 1)
   print(f"The temperature in Celsius is: {temp}°C")
elif unit == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}°F")
else:
    print(f"{unit} is an invalid unit of measurement")