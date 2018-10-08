class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        content, gi = 0, 0
        for size in s:
            while gi < len(g):
                if g[gi] <= size:
                    content += 1
                    gi += 1
                    break
                else:
                    break
        return content
