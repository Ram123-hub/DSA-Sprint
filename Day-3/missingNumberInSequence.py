def find_missing_numbers(sequence):
    n = max(sequence)

    complete_set = set(range(1,n+1))
    sequence_set =  set(sequence)

    missing_number = complete_set - sequence_set

    return sorted(missing_number)

sequence = [1, 2, 4, 5]
missing_numbers = find_missing_numbers(sequence)
print(missing_numbers)  #