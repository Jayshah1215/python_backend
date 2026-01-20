p=float(input("Enter p number:"))
r=float(input("Enter  r number:"))
t=float(input("Enter  t number:"))

amount=p*(1+r/100)*t
ci=amount-p
print("Amount:",amount)
print("Compond INterest",ci)