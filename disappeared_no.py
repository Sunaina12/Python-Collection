'''Given an array nums of n integers where nums[i] is in the range [1, n],
return an array of all the integers in the range [1, n] that do not appear in nums.'''

nums = [4,3,2,7,8,2,3,1]
# n=nums[0]
# for i in range(1,len(nums)):
#     if nums[i]>n:
#         n=nums[i]
n=len(nums)
tmp=[]
res=[]
for i in range(1,n+1):
    tmp.append(i)
print(tmp)
c=0
for i in range(0,len(tmp)):
    for j in range(len(nums)):
        if tmp[i]!=nums[j]:
            c=0

        else:
            c=1
            break
    if c==0:
        res.append(tmp[i])
print(res)

'''2nd Solution'''

n = len(nums)
res = []
val = 1

while val <= n:
    c = 0
    if val in nums:
        c = 1 9939367057

    if c == 0:
        res.append(val)
    val = val + 1
print(res)