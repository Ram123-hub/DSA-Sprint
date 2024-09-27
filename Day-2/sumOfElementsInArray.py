def sumElements(arr):
    total_sum = 0  # Avoid using `sum` as it is a built-in function
    n = len(arr)   # Get the length of the array, not the variable `sum`
    
    if n == 0:
        return None
    
    for i in range(n):
        total_sum += arr[i]
    
    return total_sum

arr = [1, 2, 3, 4, 5]
print(sumElements(arr))  # Output: 15
