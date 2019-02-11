class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # two pointer
        if len(nums) < 3:
            return
        nums.sort()
        result = nums[0] + nums[1] + nums[2] - target
        for i in range(0, len(nums)-2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                # print(tmp)
                if tmp == target:
                    return target
                elif tmp > target:
                    k -= 1
                else:
                    j += 1
                if abs(tmp - target) < abs(result-target):
                    result = tmp
        return result
