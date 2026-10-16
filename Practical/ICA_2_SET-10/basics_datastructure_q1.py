##Q1. [Python Basics & Data Structures] Let t = (3, 1, 3, 2, 3). Print the count of 3, the index of 2, and the length, maximum and minimum of the tuple. State in a comment whether t.append(4) is possible and why.

t = (3, 1, 3, 2, 3)

print("Count of 3:", t.count(3))
print("Index of 2:", t.index(2))
print("Length:", len(t))
print("Maximum:", max(t))
print("Minimum:", min(t))

# t.append(4) is not possible because tuples are immutable.