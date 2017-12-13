class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
		#自己写的解法，不够简洁
        uni = set(candies)
        if len(uni) > (len(candies)/2):
            return len(candies) / 2
        else:
            return len(uni)

	def distributeCandies1(self, candies):
		return min(len(candies) / 2, len(set(candies)))   #利用min函数，简洁很多