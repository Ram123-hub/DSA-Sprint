def fibonacci_in_range(start , end):
    fib_sequence = []
    a, b =0 , 1

    while a <= end:
        if a>= start:
            fib_sequence.append(a)
        a,b = b, a+b
    return fib_sequence
start = 10
end = 100
result = fibonacci_in_range(start, end)
print(f"Fibonacci numbers between {start} and {end}: {result}")