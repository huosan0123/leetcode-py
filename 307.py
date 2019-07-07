class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.arr = [0] * (self.n*2)
        for i in range(self.n):
            self.arr[i+self.n] = nums[i]
        for i in range(self.n-1, 0, -1):
            self.arr[i] = self.arr[i*2] + self.arr[i*2+1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        i += self.n
        ori = self.arr[i]
        self.arr[i] = val
        while i > 1:
            self.arr[i/2] += val - ori
            i /= 2
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        ans = 0
        i += self.n
        j += self.n
        if i > j:
            return 0
        while i <= j:
            if i % 2:
                ans += self.arr[i]
                i += 1
            if j % 2 == 0:
                ans += self.arr[j]
                j -= 1
            i /= 2
            j /= 2
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
