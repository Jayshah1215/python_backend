#find sqaure and store in another list
ans=[]
lst1=[1,22,6]
#for i in lst1:
#    ans=[].append(i*i)
ans=[i*i for i in lst1 if i %2==0]
print(ans)

