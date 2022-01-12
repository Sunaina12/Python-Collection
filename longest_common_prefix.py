def longest(list_arr):
    if list_arr==0:
        return 0
    if list_arr==1:
        return list_arr[0]
    list_arr.sort()
    n=len(list_arr)

    min_lenght=min(len(list_arr[0]),len(list_arr[n-1]))
    i=0
    while i<min_lenght and list_arr[0][i]==list_arr[n-1][i]:
        i=i+1
    res=list_arr[0][0:i]

    print(res)
longest(["dog","racecar","car"])
