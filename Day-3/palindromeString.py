def expand_around_center(s ,left ,right):
    while left >= 0 and right < len(s)  and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def largest_palindrome(s):
    if len(s) == 0:
        return ""
    
    longest_palindrome= ""

    for i in range(len(s)):
        palindrome_odd = expand_around_center(s , i , i)
        palindrome_even = expand_around_center(s , i , i + 1)

        if len(palindrome_odd) > len(longest_palindrome):
            longest_palindrome = palindrome_odd
        if len(palindrome_even) > len(longest_palindrome):
            longest_palindrome = palindrome_even
    
    return longest_palindrome

input_string = "babad"
result = largest_palindrome(input_string)
print(f"Largest palindrome in '{input_string}' is: '{result}'")