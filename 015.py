class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            while j < k:
                # print(ans, i, j, k)
                tri_sum = nums[i] + nums[j] + nums[k]
                if tri_sum == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    # to avoid duplicates at end
                    while j < k and k > 0 and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                    # to avoid duplicates at begin
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1    # move both j k to another pos
                elif tri_sum > 0:
                    k -= 1
                else:
                    j += 1
        return ans
        
