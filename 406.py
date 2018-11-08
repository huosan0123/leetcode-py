class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: -x[0])
        ans = []
        for p in people:
            ans.insert(p[1], p)
        return ans
        
思路并不是shortest人的位置。代码上更可行的是思考tallest。
首先 按照 h 排序，同h的按照k排序。
然后直接插入
