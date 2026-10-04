number1 = float(input("ENTER FIRST NUMBER: "))
number2 = float(input("ENTER SECOND NUMBER: "))
operation = input("ENTER OPERATION (+, -, *, /): ")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2
else:
    print("INVALID OPERATION")

print("THE RESULT IS:", result)
