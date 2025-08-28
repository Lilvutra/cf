#might correct code
num_cases = int(input())
results = []
for _ in range(num_cases):
    num = int(input())
    tens_digit = num // 10
    units_digit = num % 10

    # Calculate and print their sum
    sum_digits = tens_digit + units_digit
    results.append(sum_digits)
for result in results:
    print(result)