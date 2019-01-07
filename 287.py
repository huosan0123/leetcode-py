class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1, p2 = nums[0], nums[0]
        # python don't have do while
        # 找到两个指针的交点
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break
        # 因为是确定有重复，所以这里不用else
        
        # 找到环的入口,解题方案真的贼像142
        # 
        pt1, pt2 = nums[0], p2
        while pt1 != pt2:
            pt1 = nums[pt1]
            pt2 = nums[pt2]
            
        return pt1
