'''Given a fixed-length integer array arr, duplicate each occurrence of zero,
 shifting the remaining elements to the right.'''
'''Without In Place'''
#arr=[1,0,2,3,0,4,5,0]
arr=[1,2,3]
n=len(arr)
result=[None]*n
j=0
for i in range(len(arr)):
    try:
        if arr[i]==0:
            result[j]=arr[i]
            j=j+1
            result[j]=0
        else:
            result[j]=arr[i]
        j=j+1
    except:
        break
print(result)

'''Constraint : In Place,,,Means We can't use another array n return anything'''





