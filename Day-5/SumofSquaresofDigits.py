import math

def sumOfSquaresOfDigit(number):
    total_sum = 0
    while number > 0:
        rem = number % 10
        square_num = rem ** 2  
        total_sum += square_num
        number = number // 10  
    return total_sum

number = int(input("Enter a number"))
print(sumOfSquaresOfDigit(number))