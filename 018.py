class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            f0 = nums[i]
            if i > 0 and f0 == nums[i-1]:
                continue
            
            tar3 = target - f0
            for j in range(i+1, len(nums)):
                f1 = nums[j]
                if j >i+1 and f1 == nums[j-1]:
                    continue
                
                tar2 = tar3 - f1
                l, r = j+1, len(nums)-1
                while l < r:
                    if nums[l] + nums[r] == tar2:
                        ans.append([f0, f1, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif nums[l] + nums[r] < tar2:
                        l += 1
                    else:
                        r -= 1
        return ans
