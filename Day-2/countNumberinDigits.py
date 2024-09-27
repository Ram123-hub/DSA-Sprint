def count_digits(number):
    number = abs(number)
    
    if number ==0 :
        return 1
    
    count = 0 
    while number > 0 :
        count += 1
        number //=10
    return count

number = 12345
result = count_digits(number)
print(f"The number {number} has {result} digits.")