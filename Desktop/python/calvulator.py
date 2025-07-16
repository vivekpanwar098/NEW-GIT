# Simple Calculator in Python
#addtion x+y
def add(x, y):
    return x + y
#subtraction x-y
def subtract(x, y):
    return x - y
#multiply x*y
def multiply(x, y):
    return x * y
#divide x/y 
def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y
# all operation 
print("Select operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")
# one operation is selected
choice = input("Enter choice (1/2/3/4): ")
#enter first input and second input 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#if or elif condition you choice 1 /2 /3 /4 then your result is here
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")
