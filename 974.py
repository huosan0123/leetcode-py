class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # 一种数学的解法吧
        mod = [0] * K
        cursum = 0
        for i in A:
            cursum += i
            mod[cursum%K] += 1
        ans = 0
        
        for i in range(K):
            if mod[i] > 0:
                ans += mod[i] * (mod[i]-1) / 2
        # add the elements which are divisible by k itself 
        # i.e., the elements whose sum = 0 
        return ans + mod[0]
