class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bits = [[0, 0] for _ in range(32)]
        
        for n in nums:
            for i in range(32):
                bits[i][n%2] += 1
                n >>= 1
        
        return sum(x*y for x, y in bits)
        
