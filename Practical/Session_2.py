elements = int(input("Enter the number of elements: "))

list = []

for i in range(elements):
    num = int(input("Enter element {}: ".format(i + 1)))
    list.append(num)

print("List of elements:", list)
print("the greatest number is:", max(list), "the smallest number is:", min(list))
list.sort()
print("min and max: ", list[0], "and", list[-1])

list1 = [1, 2, 3]
list1[0], list1[-1] = list1[-1], list1[0] 

print("List after swapping first and last elements:", list1)

tuple1 = ("sub1", "sub2", "sub3", "sub4", "sub5")
for i in tuple1:
    print(i, end="\n")

    