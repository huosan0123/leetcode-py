class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = 0
        ans = 0
        for i in nums:
            if i:
                tmp += 1
                if tmp > ans:   #here could shorten to ans = max(ans, tmp)
                    ans = tmp
            else:
                tmp = 0
        return ans