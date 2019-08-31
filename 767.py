import heapq
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        cnts = [(-S.count(x), x) for x in set(S)]
        ans = []
        heapq.heapify(cnts)
        while cnts:
            cnt, ch = heapq.heappop(cnts)
            if len(cnts) == 0:
                if  cnt <= -2:
                    return ""
                else:
                    ans.append(ch)
                    return "".join(ans)
            v, k = heapq.heappop(cnts)
            ans.append(ch)
            ans.append(k)
            cnt += 1
            v += 1
            if cnt < 0:
                heapq.heappush(cnts, (cnt, ch))
            if v < 0:
                heapq.heappush(cnts, (v, k))
        return "".join(ans)
                
