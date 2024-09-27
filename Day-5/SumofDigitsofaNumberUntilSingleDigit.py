def sumOfSingleUnitDigit(number):
    while number >= 10:
        digit_sum = 0
        while number > 0:
            digit_sum += number % 10  # Add the last digit to digit_sum
            number = number // 10  # Remove the last digit from the number by updating `number`
        number = digit_sum  # Update `number` to the sum of its digits
    return number

number = 9875
print(sumOfSingleUnitDigit(number))  # Output: 2
