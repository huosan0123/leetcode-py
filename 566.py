class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        else:
            ori = []
            for i in range(m):
                for j in range(n):
                    ori.append(nums[i][j])
            ans = []
            for i in range(r):
                tmp = []
                for j in range(c):
                    tmp.append(ori[i * c + j])
                ans.append(tmp)
            return ans
"""
not the best solution because I used extra space. The best way is without extra space
"""


def matrixReshape1(self, nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]     This is short, but cost more time
    """
    import numpy as np
    try:
        return np.reshape(nums, (r, c)).tolist()
    except:
        return nums