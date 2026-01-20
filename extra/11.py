name = input("Enter a string: ")

digits = 0
letters = 0

for ch in name:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1

print("Digits =", digits)
print("Letters =", letters)
