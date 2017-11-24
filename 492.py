class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
		#自己写的代码会超时。因为是o(n)
        from math import sqrt
        half = int(sqrt(area))
        ans = [half, half]
        while ans[0] * ans[1] != area:
            if ans[0] * ans[1] > area:
                ans[1] -= 1
            else:
                ans[0] += 1
        return ans
	#下面解法是O(sqrt(n))的，所以会快很多！！！！！
	#unexpected indent是缩进错误
	def constructRectangle(self, area):
		mid = int(math.sqrt(area))
        while area%mid != 0:
            mid -= 1
        return [area/mid, mid]