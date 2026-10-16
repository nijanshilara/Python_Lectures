##Q3. [Control Flow & Loops] Accept an age and print the category: Child (below 13), Teenager (13-19), Adult (20-59) or Senior Citizen (60 and above), using if-elif-else.

age = int(input("Enter your age: "))
if age < 13:
    print("You are a child.")
elif age < 19:
    print("You are a teenager.")
elif age < 59:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
