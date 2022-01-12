def isValid(str):
    open_paranthese=['(','{','[']
    close_paranthese=[')','}',']']

    stack=[]
    for val in str:
        if val in open_paranthese:
            stack.append(val)
        elif val in close_paranthese:
            pos=close_paranthese.index(val)

            if len(stack)>0 and open_paranthese[pos]==stack[len(stack)-1]:
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True
    else:
        return False

print(isValid('()'))