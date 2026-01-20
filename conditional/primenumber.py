
number = int(input("Enter a number:"))
temp=1
for i in range(2,number):
    if number%i==0:
        temp=1
        print("Not a prime")
        break
    else:
        temp=0
if temp==0: 
        print("prime")

