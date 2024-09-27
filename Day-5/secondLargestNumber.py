def second_largest(array):
    largest = second_largest = float('-inf')  # Start with the smallest possible value
    
    for num in array:
        if num > largest:
            second_largest = largest  # Update second largest
            largest = num  # Update largest
        elif largest > num > second_largest:
            second_largest = num  # Update second largest
    
    return second_largest

# Example usage
array = [10, 20, 4, 45, 99]
print(second_largest(array))  # Output: 45
