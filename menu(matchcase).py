print("------Menu-----")
print("1. Addition")
print("2. Substraction")
print("3. multiplication")
print("4. Division")

choice =int(input("Enter your choice:"))
match choice:
    case 1:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter Second number:"))
        print(f"Addition: {num1+num2}")
    case 2:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter Second number:"))
        print(f"Substraction: {num1-num2}")
    case 3:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter Second number:"))
        print(f"Multiplication : {num1*num2}")
    case 4:
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter Second number:"))
        print(f"Division: {num1/num2}")