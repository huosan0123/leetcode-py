class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k==n or k==0:
            ans = [i for i in range(1, k+1)]
            return [ans]

        # c(n-1, k-1)，所以每一个还需要添加最后的n进去
        res = self.combine(n-1, k-1)
        for r in res:
            r.append(n)

        # 这是用前面0< x <= n-1 的数字，形成的k个数的 组合
        resb = self.combine(n-1, k)

        res.extend(resb)
        return res
