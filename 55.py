class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums)==1:
            return True
        
        pre = nums[0]
        for i in range(1, len(nums)):
            if pre == 0:
                return False
            else:
                pre = max(pre-1, nums[i])
        
        return True
