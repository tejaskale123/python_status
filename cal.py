print("\n--- Basic Calculator ---")
print("Enter 'q' anytime to quit.\n")

while True:
    operator = input("Enter an operator (+ - * /): ")
    if operator == 'q':
        print("Calculator stopped. Goodbye!")
        break

    num1 = input("Enter the 1st number: ")
    if num1 == 'q':
        print("Calculator stopped. Goodbye!")
        break
    num1 = float(num1)

    num2 = input("Enter the 2nd number: ")
    if num2 == 'q':
        print("Calculator stopped. Goodbye!")
        break
    num2 = float(num2)

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
