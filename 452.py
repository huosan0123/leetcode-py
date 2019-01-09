class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ballons = sorted(points, key=lambda x:x[1])
        ans, n = 0, len(ballons)-1
        i = 0
        while (i < n):
            j = i
            while i < n and ballons[j][1] >= ballons[i+1][0]:
                i += 1
            else:
                ans += 1
                i += 1
                
        if i == n:
            ans += 1
        return ans
    
    
    def findMinArrowShots(self, points):
        # 这份代码真的精髓！！！简单透彻
        ballons = sorted(points, key=lambda x:x[1])
        ans = 0
        end = -float("inf")
        for i in ballons:
            if i[0] > end:
                ans += 1
                end = i[1]
        return ans
