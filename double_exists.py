class Solution:
    def checkIfExist(self, arr) -> bool:
        for i in range(len(arr)):
                for j in range(len(arr)):
                    if 2*arr[i]==arr[j] and i!=j :
                        return True
s=Solution()
s.checkIfExist([10,2,5,3])