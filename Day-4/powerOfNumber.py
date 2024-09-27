def power(exponent , base):
    return base**exponent


base =int(input('Enter base: '))
exponent = int(input('Enter exponent: '))
result = power(base, exponent)
print(f"{base} raised to the power of {exponent} is {result}")