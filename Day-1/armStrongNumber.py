def is_armstrong(num):
    num_str = str(num) 
    num_digits = len(num_str) 
    
   
    sum_of_powers = 0
    
  
    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits  
    
    return sum_of_powers == num  
# Example usage:
num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
