choice = int(input("1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\nEnter your choice: "))

if choice == 1:
    F = float(input("Enter temperature in Fahrenheit: "))
    C = (5/9) * (F - 32)
    print("Temperature in Celsius =", C)

elif choice == 2:
    C = float(input("Enter temperature in Celsius: "))
    F = C * 9/5 + 32
    print("Temperature in Fahrenheit =", F)

else:
    print("Invalid choice")
