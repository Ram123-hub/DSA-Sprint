def is_perfect_numbers(num):
    if num<= 1:
        return False
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i 
    return divisors_sum

number = 28
if is_perfect_numbers(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")