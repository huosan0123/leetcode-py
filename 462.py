class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        s = sorted(nums)
        
        def compute(x):
            move = 0
            for i in nums:
                move += abs(i-x)
            return move
        
        idx = []
        if len(nums) % 2 == 0:
            mid = len(nums) / 2
            ans = min(compute(s[mid-1]), compute(s[mid]) )
        else:
            mid = (len(nums) - 1) / 2
            ans = compute(s[mid])
        return ans
        
