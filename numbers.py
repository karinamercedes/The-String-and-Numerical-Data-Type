# Ask the user to enter three different integers.
# Then print out:
#	○ The sum of all the numbers
#	○ The first number minus the second number
#	○ The third number multiplied by the first number
#	○ The sum of all three numbers divided by the third number

# Ask the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculations
sum_of_numbers = num1 + num2 + num3
difference_first_two = num1 - num2
product_first_and_third = num1 * num3
expression = (num1 + num2 + num3) / num3

#Print
print(f"The sum of all numbers: {sum_of_numbers}")
print(f"The first number minus the second number: {difference_first_two}")
print(f"The third number multiplied by the first number: {product_first_and_third}")
print(f"The sum of all three numbers divided by the third number: {expression}")
