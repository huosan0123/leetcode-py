# copied from other's solution

class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        back = 1
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            back *= nums[i+1]
            ans[i] *= back
        
        return ans
