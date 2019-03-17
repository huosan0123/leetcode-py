class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        pre, ans = 0, []
        for i in range(len(nums)):
            if nums[i] > nums[i-1] + 1:
                if i-1 == pre:
                    ans.append(str(nums[pre]))
                else:
                    ans.append("%d->%d"%(nums[pre], nums[i-1]))
                pre = i

        if i == pre:
            ans.append(str(nums[-1]))
        else:
            ans.append("%d->%d"%(nums[pre], nums[-1]))
        return ans
