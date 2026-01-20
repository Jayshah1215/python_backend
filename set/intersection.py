num1={1,2,3,4}
num2={11,2,44,4}
num4={1,2,44}
num3=num1.intersection(num2,num4)
num3=num1|num2|num4
print(num3)

num3=num2.difference(num1)
print(f"Difference {num3}")