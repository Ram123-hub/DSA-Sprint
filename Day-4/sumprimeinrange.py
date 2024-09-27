def is_prime(num):

    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def sum_of_primes_in_range(range_start, range_end):

    prime_sum = 0
    for num in range(range_start, range_end + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum


input_range = [1, 10]
result = sum_of_primes_in_range(input_range[0], input_range[1])
print(f"Input: range = {input_range}")
print(f"Output: {result}")
