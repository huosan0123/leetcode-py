class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[n-1]:
                nums[n] = nums[i]
                n += 1
            else:
                if n-2>=0 and nums[i] != nums[n-2]:
                    nums[n] = nums[i]
                    n += 1
                if n == 1:
                    n += 1
        
        return n
