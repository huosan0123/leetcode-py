class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 比较的时候，<=很重要，不然全1就有问题
        c1 = c2 = float("inf")
        for n in nums:
            if n <= c1:
                c1 = n
            elif n <= c2:
                c2 = n
            else:
                return True
        return False
