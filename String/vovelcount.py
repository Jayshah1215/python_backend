name=input("Enter a name:")
count=0
for i in name:
    if i in "aeiouAEIOU":
        count+=1
print(f"Number of vovel in string : {count}")