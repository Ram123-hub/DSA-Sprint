def isprime(num):
    if  num <= 1:
        return False
    for i in range(2 , int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def primes_in_range(start, end):
    primes =[]
    for num in range(start, end+1):
        if isprime(num):
            primes.append(num)
    return primes

start = 10
end = 50
prime_numbers = primes_in_range(start, end)
print(f"Prime numbers between {start} and {end}: {prime_numbers}")