num=int(input("Enter a number:"))
for i in range(num):
    for j in range(num,i,i-1):
        print(j,end=" ",)
    print()