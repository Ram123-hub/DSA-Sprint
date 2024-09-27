def palindrome(string):
    new_str = string[::-1]

    if (new_str == string):
        print("String is palindrome")


def is_palindrome(string):
    reversed_str = " "
    for char in string:
        reversed_str = char + reversed_str
    
    if(reversed_str == string):
        print("String is palindrome")
    

string = input("Enter an string or number: ")
palindrome(string)
is_palindrome(string)