print("choose between the following options: ")
print("Celsius to Fahrenheit: 1")
print("Fahrenheit to Celsius: 2")
input = int(input("Enter the number of the option: "))

def tempreture_convertor(temp, unit):
    if unit == 1:
        return (temp * 9/5) + 32
    elif unit == 2
        return (temp - 32) * 5/9
    else:
        return "Error: Unknown unit."
    