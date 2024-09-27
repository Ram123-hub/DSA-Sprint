def counting_vowels_and_consonants(string):
    vowel_count = 0
    consonant_count = 0
    vowels = ["a", "e", "i", "o", "u"]

    for char in string.lower():  
        if char.isalpha(): 
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Example
string = input("Enter a string: ")
vowel_count, consonant_count = counting_vowels_and_consonants(string)
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
