class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = set(nums1) & set(nums2)
        ans = []
        for item in a:
            ans.append(item)
        return ans

    """
    a one-line solution
    return list(set(nums1) & set(nums2)) 
    """