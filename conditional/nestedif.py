age = int(input("Enter age:"))
weight =int(input("Enter weight:"))
if age>=18:
    if weight>=55:
        print("User is able to donate blood")
    else:
        print("User is unabkke to donate blood due to under weight")
else:
    print("user is  unable to donate blood due to minor")