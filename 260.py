class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Ignore space complexity, it's so easy.
        from collections import Counter
        freq = Counter(nums)
        ans = [k for k in freq if freq[k] == 1]
        return ans
        
    def singleNumber(self, nums):
        # bit maniputation, brilliant.
        # nums 里面所有元素 xor 后的结果肯定是 = 3^5的。因为这两个数不一样，所以结果必定不为0
        # 所以xor的结果至少一位是1. 我们要找到一个 1 的位置，产生一个mask。
        # 这个mask只有一个bit位是1，其余位置都是0.
        # 利用这个mask可以把nums的数字分成两个部分，每个部分都是[1, 1, 3]这种形式
        # 所以对每个部分直接 xor 就能找到 唯一的那个数字了
        
        # 因为是xor，所以xor初始=0 没毛病。a, b 相同
        xor = 0
        for i in nums:
            xor ^= i
        
        mask = 1
        while (xor & mask == 0):
            mask = mask << 1
        
        a, b = 0, 0
        for n in nums:
            if n & mask == 0:
                a ^= n
            else:
                b ^= n
        return [a, b]
