'''Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.'''

nums = [19, -10, 20, 14, 2, 16, 10]
import sys
# tmp=list(set(sorted(nums)))
# print(tmp)
# try:
#     print(tmp[-3])
# except:
#     print(tmp[-1])

'''2nd Way'''
# max=nums[0]
# max2=-1
# max3=-1
# for i in range(len(nums)):
#     if nums[i]>max:
#         max=nums[i]
# for i in range(len(nums)):
#     if nums[i]>max2 and nums[i]<max:
#         max2=nums[i]
# for i in range(len(nums)):
#     if nums[i]>max3 and nums[i]<max2:
#         max3=nums[i]
# print(max,max2,max3)
# try:
#     print(max3)
# except:
#     print(max)

print(-sys.maxsize)
tmp=list(set(nums))
first=nums[0]
print(tmp)
second=-sys.maxsize
third=-sys.maxsize

for i in range(len(nums)):
    if len(tmp)>=3:
        if nums[i]>first:
            third=second
            second=first
            first=nums[i]
        elif nums[i]>second:
            third=second
            second=nums[i]
        elif nums[i]>third:
            third=nums[i]
    else:
        if nums[i]>first:
            third=nums[i]
print(third)