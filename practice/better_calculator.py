first_num = float(input("Enter first number:"))
op = input("Enter operator:")
second_num = float(input("Enter second number: "))

if op == "+":
    print(first_num + second_num)
elif op == "-":
    print(first_num - second_num)
elif op == "/":
    print(first_num / second_num)
elif op == "*":
    print(first_num * second_num)
else:
    print("Invalid operator")