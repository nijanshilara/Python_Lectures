num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print("Sum =", num1 + num2)

elif operator == "-":
    print("Difference =", num1 - num2)

elif operator == "*":
    print("Product =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Cannot divide a number by zero")

else:
    print("Invalid operator")