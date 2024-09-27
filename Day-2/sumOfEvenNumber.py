def sum_of_even_numbers(start ,end):
    even_sum = 0
    for num in range(start, end+1):
        if num % 2 == 0:
            even_sum += num
    return even_sum

start = 1
end = 10
result = sum_of_even_numbers(start, end)
print(f"Sum of even numbers between {start} and {end}: {result}")
    
    