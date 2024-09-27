def fibonacci_series(limit):
    if limit <= 1 :
        return 1
    else:
        return fibonacci_series(limit-1 ) + fibonacci_series(limit-2)


terms = int(input("Enter the number of terms: "))
for i in range(terms):
    print(fibonacci_series(i), end=" ")