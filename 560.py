class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 自己想出来的O(n2)的解法用python TLE，c++能过，显示了C++的强大之处；
        # 下面这个字典保存的是很帮的呀
        dic = {}
        dic[0] = 1
        cursum = ans = 0
        for n in nums:
            cursum += n
            if cursum - k in dic:
                ans += dic[cursum-k]
            if cursum in dic:
                dic[cursum] += 1
            else:
                dic[cursum] = 1
        return ans
