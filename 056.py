# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        inters = sorted(intervals, key=lambda x:(x.start, x.end))
        # print(inters)
        ans = [inters[0]]
        for i in range(1, len(inters)):
            if inters[i].start <= ans[-1].end:
                if ans[-1].end < inters[i].end:
                    ans[-1].end = inters[i].end
            else:
                ans.append(inters[i])
        return ans
