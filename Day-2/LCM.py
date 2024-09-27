
import math


def lcm_using_gcd(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_iterative(a,b):
    max_ab = max(a,b)
    lcm = max_ab
    while lcm % a != 0 or lcm % b != 0:
        lcm += max_ab
    return lcm

print(lcm_using_gcd(12,18))
print(lcm_iterative(12, 18))