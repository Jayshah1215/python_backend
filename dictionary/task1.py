dict1={"India":"delhi","newzealand":"amsterdam","France":"Paris"}
print(dict1)
print(dict1["India"])

print(dict1.keys())
print(dict1.values())
print(dict1.items())


print("Iterative keys:")
for i in dict1.keys():
    print(i)


print("Iterative values:")
for i in dict1.values():
    print(i)

print("Iterative items:")
for i,j in dict1.items():
    print(i,j)
