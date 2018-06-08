class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
		当前屋子是否可偷，前一个屋子的cost vs 前两个屋子的cost+此屋子；
		自己写的是对的，但是前面判断很明显有改进空间
        """
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a, b = nums[0], max(nums[0:2])
        for i in range(2, len(nums)):
            c = max(b, a + nums[i])
            a, b = b, c
        return c
		
	def rob(self, nums):
        last, now = 0, 0  # 相当于前面放两个空房间
        for i in nums: last, now = now, max(last + i, now)
        return now