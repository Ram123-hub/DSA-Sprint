def factorial(num):
    sum = 0
    if num==0 or num==1:
        return 1 
    else:
        factorial =  num * factorial(num-1)
    
    rem = factorial % 10 
    sum += rem
    return sum 

    



number = 4
print(f"Sum of factorials up to {number} is: {factorial(number)}")