class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        # copied the idea from solutions
        """
        self.he = [0] * (len(nums)+1)
        for i, num in enumerate(nums):
            self.he[i+1] += self.he[i] + num

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.he[j+1]-self.he[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
