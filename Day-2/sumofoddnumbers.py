def sumofoddnumbers(start, end):
    odd_sum = 0
    for num in range(start , end +1):
        if num % 2 != 0 :
            odd_sum += num
    return odd_sum

start = 1
end = 10
result = sumofoddnumbers(start, end)
print(f"Sum of even numbers between {start} and {end}: {result}")