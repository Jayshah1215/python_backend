count=0
list_name=['meet','mohit','naresh','harsh']
for i in list_name:
    if i.startswith('m'):
        print(i)
        count+=1
print(f"Total string start with m: {count}")