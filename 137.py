class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a, b = 0, 0
        for i in nums:
            a, b = (a & ~b & ~i) | (~a & b & i), (~a & b & ~i) | (~a & ~b & i)
        return a | b
