class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums or s <= 0 or min(nums)<=0:
            return 0

        i, j, n = 0, 0, len(nums)
        ssum, minlen = nums[0], n + 1
        while i < n:
            if j < n:
                if ssum < s:
                    j += 1
                    if j < n:
                        ssum += nums[j]
                else:
                    minlen = min(minlen, (j - i)+1)
                    ssum -= nums[i]
                    i += 1
            else:
                break
        return 0 if minlen == n+1 else minlen
        
