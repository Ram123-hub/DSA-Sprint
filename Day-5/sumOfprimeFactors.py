def sum_of_prime_factors(number):
    prime_factors = set()  # Using a set to store unique prime factors
    # Check for number of 2s that divide number
    while number % 2 == 0:
        prime_factors.add(2)
        number //= 2
    
    # Check for odd factors from 3 to sqrt(number)
    for i in range(3, int(number**0.5) + 1, 2):
        while number % i == 0:
            prime_factors.add(i)
            number //= i
    
    # If number is a prime number greater than 2
    if number > 2:
        prime_factors.add(number)
    
    return sum(prime_factors)

# Example usage
number = 12
print(sum_of_prime_factors(number))  # Output: 5
