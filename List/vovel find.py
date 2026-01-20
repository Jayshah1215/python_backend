lst_city=['ahmedabad','surat','rajkot']
for i in lst_city:
    for j in i:
        if j in "aeiouAEIOU":
            print(f"Vovel in :{i}")
            break
        
