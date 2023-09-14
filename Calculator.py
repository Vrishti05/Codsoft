def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y

print("========================|| SIMPLE CALCULATOR ||========================")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")

choice = input("Enter choice: ")

if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
        operation = "addition"
    elif choice == '2':
        result = subtract(num1, num2)
        operation = "subtraction"
    elif choice == '3':
        result = divide(num1, num2)
        operation = "division"
    else:
        result = multiply(num1, num2)
        operation = "multiplication"

    print(f"{operation} of given numbers are : {result}")
else:
    print("Invalid input. Please select a valid operation (1/2/3/4).")
