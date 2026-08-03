# Solution 1: Count the vowels in a string

text = input("Enter a string: ")
vowel_count = 0

for letter in text.lower():
    if letter in "aeiou":
        vowel_count += 1

print("Number of vowels in the string:", vowel_count)


# Solution 2: Join two strings together

first_text = input("Enter the first string: ")
second_text = input("Enter the second string: ")

print("The concatenated string is:", first_text + " " + second_text)