
def calculator(num1, num2, math_operation):
    if math_operation == "sum":
        return num1 + num2
    elif math_operation == "difference":
        return num1 - num2
    elif math_operation == "multiple":
        return num1 * num2
    elif math_operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Unknown operation."
    
    
print(calculator(5, 3, "sum"))