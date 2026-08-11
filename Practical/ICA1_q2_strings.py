##Strings
##Let word = "level". Check whether it's a palindrome by comparing it with its reverse slice
##Check program again with a non-palindrome word, and show both outputs

word = "level"

if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

word = "nijanshi"
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")
