class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        le = len(nums)
        return self.buildBST(nums, 0, le-1)
        
    def buildBST(self, nums, l, r):
        if l > r:
            return None
        elif l == r:
            p = TreeNode(nums[l])
            return p
        else:
            mid = (l + r) // 2
            p = TreeNode(nums[mid])
            p.left = self.buildBST(nums, l, mid-1)
            p.right = self.buildBST(nums, mid+1, r)
            return p
