def lengthOfLastWord(s):
    i = len(s.strip()) - 1
    length = 0
    try:
        while s.strip()[i] != ' ':
            length += 1
            i = i - 1
        return length
    except:
        return len(s.strip())
print(lengthOfLastWord('a'))

a=[6,7,8,9]
a.insert(1,10)
print(a)
a.pop(1)
print(a)