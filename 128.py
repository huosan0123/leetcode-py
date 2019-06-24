class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. 没理解题目要干嘛，看了答案才知道；2. 理解了要干嘛之后要能够想到出现过的不会出现在其他数字的lcs里面
        nums = set(nums)
        max_len = 0
        while nums:
            x = nums.pop()
            tmp_len = 1
            
            left, right = x - 1, x+1
            while left in nums:
                tmp_len += 1
                nums.remove(left)
                left -= 1

            while right in nums:
                tmp_len += 1
                nums.remove(right)
                right += 1
            max_len = max(max_len, tmp_len)
        return max_len
