class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) <=1:
            return 0

        jump, pre, max_pre = 1, nums[0], nums[0]
        for i in range(1, len(nums)-1):
            max_pre = max(max_pre-1, nums[i])
            if pre == 1:
                pre = max_pre
                jump += 1
            else:
                pre -= 1
                
        return jump
        
        
