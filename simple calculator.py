print("Enter two numbers: ")
num1 = float(input())
num2 = float(input())

print("Enter an operator (+, -, *, /): ")
operator = input()

if operator == '+':
   result = num1 + num2
   print(num1, "+", num2, "=", result)

elif operator == '-':
   result = num1 - num2
   print(num1, "-", num2, "=", result)

elif operator == '*':
   result = num1 * num2
   print(num1, "*", num2, "=", result)

elif operator == '/':
   result = num1 / num2
   print(num1, "/", num2, "=", result)

else:
   print("Invalid operator. Please enter a valid operator (+, -, *, /).")
