# Read the two-digit integer input
num = int(input().strip())

# Extract the two digits
tens_digit = num // 10
units_digit = num % 10

# Print the two digits
print(tens_digit, units_digit)

# Calculate and print their sum
sum_digits = tens_digit + units_digit
print(sum_digits)
