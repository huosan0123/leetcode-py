class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        # 这道题和Permutation的思路一样： 把当前数字 插入到已有 list 里面的 每一个位置
        # 如果 待插入的值 和 当前位置的值相同，那就跳过。
        for n in nums:
            tmp = []
            for l in ans:
                for i in range(len(l) + 1):
                    tmp.append(l[:i] + [n] + l[i:])
                    # 这个break真是精髓。
                    if i < len(l) and l[i] == n:    break
            ans = tmp
        return ans
