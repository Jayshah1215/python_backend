lst_numbers=[1,2,3,4,5,6,7,33,23]
lst_city=['ahmedabad','surat','rajkot']
#lst_numbers.clear() :op--[]
del lst_numbers[4]
print(lst_numbers)

"""
pop:
"""
print(f"Pop method:{lst_numbers.pop()}")
print(lst_numbers)

print(f"Pop method:{lst_numbers.pop(3)}")
print(lst_numbers)

#--------------------

#Remove:

print(f"Remove(4):{lst_numbers.remove(6)}")
print(lst_numbers)


#--------------------

#Reverese:

print(f"Reverse:{lst_numbers.reverse()}")
print(lst_numbers)


