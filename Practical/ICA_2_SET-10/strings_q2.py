##Q2. [Strings, I/O & Operators] Let s = "Functional Programming". Print its length, first four characters, last five characters, every second character, and the string in reverse using slicing.

s = "Functional Programming"
print("Length:", len(s)) #prints the length of the string
print("First 4 characters:", s[0:4]) #prints the first 4 characters of the string
print("Last 5 characters:", s[-5:]) #prints the last 5 characters of the string
print("Every second character:", s[::2]) #prints every second character of the string
print("Reversed string:", s[::-1]) #prints the string in reverse order
