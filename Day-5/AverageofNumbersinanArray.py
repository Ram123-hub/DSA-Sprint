def averageNumber(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        sum += arr[i] 
    
   
    average = sum / n 
    return average

array = [1, 2, 3, 4, 5]
print(averageNumber(array))  # Output: 3.0
