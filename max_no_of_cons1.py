'''Given a binary array..Calculate max no of consecutive 1's'''
arr=[1, 1, 0, 0, 1, 0, 1,0, 1, 1, 1, 1]

count=0
result=0
for i in range(len(arr)):
    if arr[i]==1:
        count=count+1
        #result=max(result,count)
        if count>result:
            result=count
    else:
        count=0

print(result)

