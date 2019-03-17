class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if min(nums) <= 0 or k <= 0:
            return 0
        count, i, j, prod = 0, 0, 0, 1
        while(j < len(nums)):
            prod *= nums[j]
            while (i <= j and prod>=k):
                prod /= nums[i]
                i += 1
            count += (j-i+1)
            j += 1
        return count
