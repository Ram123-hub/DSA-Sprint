def is_armstrong(number):
   
    digits = str(number)
    num_digits = len(digits)
    
   
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    
    return armstrong_sum == number

def find_armstrong_numbers(start, end):
   
    armstrong_numbers = []
    
    for num in range(start, end + 1):
        if is_armstrong(num):
            armstrong_numbers.append(num)
    
    return armstrong_numbers


range_start = 1
range_end = 500
result = find_armstrong_numbers(range_start, range_end)
print(result)  
