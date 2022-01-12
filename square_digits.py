'''Given an integer array nums sorted in non-decreasing order,
 return an array of the squares of each number sorted in non-decreasing order.'''

nums = [-4,-1,0,3,10]
square=[]
for i in range(len(nums)):
    square.append(nums[i]*nums[i])
print(sorted(square))

# res=square.sort()
# print(res)