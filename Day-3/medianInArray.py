def find_median(array):
    # Sort the array
    sorted_array = sorted(array)
    n = len(sorted_array)

    # Find the median based on whether the length is odd or even
    mid_index = n // 2

    if n % 2 == 1:  # If the length is odd
        median = sorted_array[mid_index]  # Middle element
    else:  # If the length is even
        median = (sorted_array[mid_index - 1] + sorted_array[mid_index]) / 2  # Average of two middle elements

    return median

# Example usage
array = [3, 1, 2, 4, 5]
median = find_median(array)
print(median)  # Output: 3
