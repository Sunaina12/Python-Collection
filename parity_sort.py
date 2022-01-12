'''Inplace'''
nums=[3,1,2,4]
n=len(nums)
j=0
for i in range(n):
    if nums[i]%2==0:
        if nums[j]%2!=0:
            temp=nums[j]
        nums[j]=nums[i]
        nums[i]=temp
        j = j + 1
print(nums)

'''with result array'''
n = len(nums)
res = []
for i in range(0, n):
    if nums[i] % 2 == 0:
        res.append(nums[i])

for i in range(0, n):
    if nums[i] % 2 != 0:
        res.append(nums[i])

print(res)