'''given a list num of nubers...Calculate the total no of values containg even digit'''

num=[437,315,322,431,686,264,442]

result=0
for val in num:
    count = 0
    while val!=0:
        val=val//10
        count=count+1
    print(count)
    if count%2==0:
        result=result+1
print(result)