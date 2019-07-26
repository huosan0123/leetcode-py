class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]  这种解法是O(NK)的，下面排序的O(n*klogk)
        """
        from collections import defaultdict
        
        dic = defaultdict(list)
        for s in strs:
            count = [0]*26
            for a in s:
                count[ord(a) - ord('a')] += 1
            dic[tuple(count)].append(s)
        
        return dic.values()
        
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        backup = []
        for s in strs:
            backup.append(''.join(sorted(s)))
        d = {}
        for i, s in enumerate(backup):
            if s in d:
                d[s].append(strs[i])
            else:
                d[s] = [strs[i]]
        
        return list(d.values())
