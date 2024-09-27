def sum_of_digits(n):
    total = 0
    for digit in str(n):  # Convert the number to a string
        total += int(digit)  # Convert each character back to an integer and add to total
    return total

# Example usage:
num = int(input("Enter a number: "))
print(f"The sum of the digits of {num} is {sum_of_digits(num)}")

def sum_of_digits(n):
    if n == 0:  # Base case
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)  # Add the last digit to the sum of the remaining digits

# Example usage:
num = int(input("Enter a number: "))
print(f"The sum of the digits of {num} is {sum_of_digits(num)}")
