def countofSpecificDigitsinaNumber(number , digit):
    number_str = str(number)
    digit_str = str(digit)

    count = number_str.count(digit_str)

    return count

    # Convert the number and digit to strings to enable easier comparison
    number_str = str(number)
    digit_str = str(digit)
    
    # Use the count method to count the occurrences of digit_str in number_str
    count = number_str.count(digit_str)
    
    return count

# Example usage
number = 122333
digit = 3
print(countofSpecificDigitsinaNumber(number, digit))