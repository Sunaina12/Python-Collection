'''Remove element from list'''
nums = [3,2,2,3]
val = 3
res=[]
count=0
for i in nums:
    if val==i:
        count=count+1
    else:
        res.append(i)
print(count,res)




