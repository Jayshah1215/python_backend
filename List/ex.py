#add int value from list
lst_numbers = [1,2,3,4,4343]
sum=0
for i in lst_numbers:
    if type(i)==int:
        sum+=i
print(f"Total element:{sum}")