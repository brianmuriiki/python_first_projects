print("WELCOME")
number1 = input("Enter the first number: ")
operator = input("Enter the operator (+, -, *, /,min,max,sqrt,**): ")
number2 = input("Enter the second number: ")

def operations():
    if operator == "+":
        return float(number1) + float(number2)
    elif operator == "-":
        return float(number1) - float(number2)
    elif operator == "*":
        return float(number1) * float(number2)
    elif operator == "/":
        if float(number2) != 0:
            return float(number1) / float(number2)
        else:
            return "Error: Division by zero is not allowed."
    elif operator == "min":
        return min(float(number1), float(number2))
    elif operator == "max":
        return max(float(number1), float(number2))
    elif operator == "sqrt":
        if float(number1) >= 0:
            return float(number1) ** 0.5
        else:
            return "Error: Cannot calculate the square root of a negative"
    elif operator == "**":
        return float(number1) ** float(number2)
    else:
        return "Error: Invalid operator."
        
    result = operations()
    print("The result is: ", result)
