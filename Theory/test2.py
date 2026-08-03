from statistics import mean

# Program 1: Find the factorial of a number

number = int(input("Enter a number: "))
factorial_result = 1

for i in range(1, number + 1):
    factorial_result *= i

print("Factorial of", number, "is:", factorial_result)


# Program 2: Display the grade based on marks

marks_obtained = int(input("Enter the marks from 0-100: "))

if 75 <= marks_obtained <= 100:
    grade = "distinction"
elif marks_obtained >= 60:
    grade = "first class"
elif marks_obtained >= 50:
    grade = "second class"
elif marks_obtained >= 35:
    grade = "pass"
elif marks_obtained >= 0:
    grade = "fail"
else:
    grade = "invalid input"

print("Grade:", grade)


# Program 3: Find the largest and average of three numbers

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

print("Largest number:", max(first_number, second_number, third_number))
print("Average:", mean([first_number, second_number, third_number]))


# Program 4: Calculate railway ticket discount

employee_status = input("Are you a railway employee? (yes/no): ")

if employee_status.lower() == "yes":
    discount_percentage = 30
else:
    passenger_age = int(input("Enter your age: "))
    if passenger_age < 18:
        discount_percentage = 20
    elif passenger_age > 60:
        discount_percentage = 25
    else:
        discount_percentage = 5

print(f"You are eligible for a discount of {discount_percentage}%.")


# Program 5: Check whether a number is prime

check_number = int(input("Enter a number: "))
prime_flag = True

if check_number < 2:
    prime_flag = False
else:
    for divisor in range(2, check_number):
        if check_number % divisor == 0:
            prime_flag = False
            break

if prime_flag:
    print(f"{check_number} is Prime")
else:
    print(f"{check_number} is Not Prime")


# Program 6: Generate the Fibonacci series

term_count = int(input("How many terms? "))
first_term, second_term = 0, 1

for i in range(term_count):
    print(first_term, end=" ")
    first_term, second_term = second_term, first_term + second_term

print()


# Program 7: Simple Calculator

print("----- Simple Calculator -----")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = int(input("Enter your choice (1-4): "))
value_one = float(input("Enter first number: "))
value_two = float(input("Enter second number: "))

if operation == 1:
    print("Result:", value_one + value_two)
elif operation == 2:
    print("Result:", value_one - value_two)
elif operation == 3:
    print("Result:", value_one * value_two)
elif operation == 4:
    if value_two != 0:
        print("Result:", value_one / value_two)
    else:
        print("Error: Division by zero is not allowed")
else:
    print("Invalid choice")


# Program 8: List operations

fruit_list = ["apple", "banana", "cherry", "date"]

print(fruit_list[0])
print(fruit_list[-1])


number_list = [1, 2, 3]

number_list.append(4)
number_list.insert(1, 1.5)
number_list.extend([5, 6])

print(number_list)


letter_list = ["A", "B", "C", "D", "E"]

letter_list.remove("B")
removed_last = letter_list.pop()
removed_first = letter_list.pop(0)

print(letter_list)


score_list = [45, 89, 12, 76, 23]

print(max(score_list))
print(min(score_list))
print(sum(score_list))
print(len(score_list))


alphabet_list = ["d", "a", "c", "b"]

print(sorted(alphabet_list))

alphabet_list.reverse()
print(alphabet_list)


values = [1, 2, 3, 4, 5, 6]
square_list = [num ** 2 for num in values if num % 2 == 0]

print(square_list)


color_list = ["red", "blue", "red", "green"]

if "blue" in color_list:
    print("Found blue!")

print(color_list.count("red"))