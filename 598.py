class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int   不够简洁
        """
        if not ops:
            return m * n     #额外考虑
        minx, miny = 40001,40001
        for op in ops:
            if op[0] < minx:
                minx = op[0]
            if op[1] < miny:
                miny = op[1]
        return (minx)*(miny)
		
		
    def maxCount(self, m, n, ops):
        #这样才够简洁
		if not ops:
			return m*n
		else:
			return min([op[0] for op in ops]) * min([op[1] for op in ops])