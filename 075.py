class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        index = 0
            
        while index < len(nums):
            if nums[index] == 0 and index > left:
                nums[index] = nums[left]
                nums[left] = 0
                left += 1
            elif nums[index] == 2 and index < right:
                nums[index] = nums[right]
                nums[right]
                right -= 1
            else:  # 前面不能index++。比如【1，0，2】这种
                index += 1
                
