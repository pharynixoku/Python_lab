from utils import square, is_even, celsius_to_fahrenheit

number = float(input("Enter a number: "))

print("square:", square(number))

if is_even(number):
     print("the number is even.")

else:
    print("The number is odd.")

print("Fahrenheit:", celsius_to_fahrenheit(number))

