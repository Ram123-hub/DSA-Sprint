# Function to calculate the factorial of a number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

# Function to calculate the sum of the digits of a number
def sum_of_digits(n):
    total_sum = 0
    while n > 0:
        rem = n % 10  # Get the last digit
        total_sum += rem  # Add the digit to the sum
        n //= 10  # Remove the last digit from n
    return total_sum

number = 4
fact_result = factorial(number)
print(f"Factorial of {number} is: {fact_result}")

# Sum of digits of the factorial
digit_sum = sum_of_digits(fact_result)
print(f"Sum of digits of {number}! is: {digit_sum}")
