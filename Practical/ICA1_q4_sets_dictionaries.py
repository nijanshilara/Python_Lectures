###[Sets & Dictionaries]
##Trace the following step by step and print the final dictionary
##d = {}; then run d["python"] = d.get("python", 0) + 1 TWICE in a row
##print final output


d = {} #creates an empty dictionary
d["python"] = d.get("python", 0) + 1 # "python" is absent, so get() returns 0; 0+1 = 1
d["python"] = d.get("python", 0) + 1 # "python" is now present, so get() returns 1; 1+1 = 2

print(d) #prints the final dictionary d
print(d.get("python", 0)) #prints the value of key "python" in dictionary d