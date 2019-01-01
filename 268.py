class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i, v in enumerate(nums):
            n = n ^ i ^ v
        return n
        
        
        
        ## n * (n+1) /2
