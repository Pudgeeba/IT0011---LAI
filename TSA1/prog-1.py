def count_characters(string):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    
    vowel_count = consonant_count = space_count = other_count = 0
    
    for char in string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char == " ":
            space_count += 1
        else:
            other_count += 1

    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Spaces: {space_count}")
    print(f"Other Characters: {other_count}")

# Example usage
input_string = input("Enter a string: ")
count_characters(input_string)
