class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        most_v = 0
        i, j = 0, len(height) - 1
        while i < j:
            v = min(height[i], height[j]) * (j - i)
            if v > most_v:
                most_v = v
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return most_v
