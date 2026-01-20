start = int(input("Enter first number: "))
end = int(input("Enter second number: "))

for num in range(start + 1, end):
    if num % 2 == 0:
        print(num, end=" ")
