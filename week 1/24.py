# Q24. Create a calculator app using if-else.

a = int (input("enter first number"))
b = int (input("enter second number"))
op = input("enter the operation(+,-,/,*)")

if op == "+":
    print(f"{a} + {b} is =", a+b)

elif op == "-":
    print(f"{a} - {b} is =", a-b)

elif op == "/":
    if b == 0:
        print("Error: Division by zero")
    else:
        print(f"{a} / {b} is =", a / b)

elif op == "*":
    print(f"{a} * {b} is =", a*b)

else:
    print("enter a valid operation")