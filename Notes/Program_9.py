age = int(input("Enter your age: "))

if 0 <= age < 5:
    print("Ticket: Free")

elif age < 12:
    print("Ticket: ₹10")

elif age < 18:
    student = input("Are you a student? (yes/no): ")

    if student.lower() == "yes":
        print("Ticket: ₹12")
    else:
        print("Ticket: ₹15")

elif age < 60:
    print("Ticket: ₹50")

elif age <= 100:
    print("Ticket: ₹10 (Senior Citizen)")

else:
    print("Invalid age")