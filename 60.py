class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        nums = range(1, n+1)
        ans = ''
        k -= 1
        while n>0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            ans += str(nums[index])
            nums.remove(nums[index])
        return ans
