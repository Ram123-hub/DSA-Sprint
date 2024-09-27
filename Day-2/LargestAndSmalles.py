def find_min_max(arr):
    if len(arr) == 0:
        return None, None  # Edge case: empty array

    smallest = largest = arr[0]

    for num in arr[1:]:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num

    return smallest, largest


def find_max_Min(arr):
    if len(arr) == 0:
        return None ,  None
    
    smallest = min(arr)
    largest = max(arr)

    return smallest, largest

# Example usage:
arr = [34, 2, 56, 7, 89, 23]
smallest, largest = find_min_max(arr)
print(f"Smallest: {smallest}, Largest: {largest}")
Smallest , Largest = find_max_Min(arr)
print(f"Smallest: {Smallest}, Largest: {Largest}")
