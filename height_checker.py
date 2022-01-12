heights = [1,1,4,2,1,3]
expected=sorted(heights)
c=0
print(expected)
for i in range(len(heights)):
    if heights[i]!=expected[i]:
       c=c+1
print(c)