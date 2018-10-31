class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 利用{}很好做，but 时间复杂度超标
        from collections import Counter
        hash_table = Counter(nums)
        a = sorted(hash_table.items(), key=lambda item: item[1], reverse=True)
        b = [i[0] for i in a[:k]]
        return b
        
    # this also works
    # [i[0] for i in Counter(nums).most_common(k)]
