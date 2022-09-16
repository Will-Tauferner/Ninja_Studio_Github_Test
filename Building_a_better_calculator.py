#Building a better calculator

num1 = float(input("enter first number: "))
op = input("Enter Operator: ")
num2 = float(input("enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
        print (num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print (num1 * num2)
else:
    print("invalid operator")