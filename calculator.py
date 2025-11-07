operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print("Result:", result)
elif operator == "-":
    result = num1 - num2
    print("Result:", result)
elif operator == "*":
    result = num1 * num2
    print("Result:", result)
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero not allowed.")
else:
    print("Invalid operator!")
