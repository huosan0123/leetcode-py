class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = {}
        for item in nums:
            if item not in ans:
                ans[item] = 1
            else:
                ans[item] += 1
        for item in ans:          #dict's operation
            if ans[item] == 1:
                return item
            
    def singleNumber2(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res
    
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)

  # n ^ n = 0; 1 ^ 2 ^ 1 = (1 ^ 1) ^ 2.
