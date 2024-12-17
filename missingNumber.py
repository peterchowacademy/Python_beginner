#User function Template for python3
class Solution:
    def missingNumber(self, arr):
        # code here
        size = len(arr)
        arr.sort()
        for i in range(size):
            if arr[i] == i+1:
                pass
            else:
                return i+1
        return size+1
case1=[1,4,3,5]
case2=[1]
case3=[1,2,4,5,8,7,9]
s = Solution().missingNumber(arr=case1)
print(s)
s2 = Solution().missingNumber(arr=case2)
print(s2)
s3 = Solution().missingNumber(arr=case3)
print(s3)

print(max(13,-3))