# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_sum = float("-inf")
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathDown(root)
        return self.max_sum
    
    def maxPathDown(self, root):
        if not root:    return 0
        lsum = max(0, self.maxPathDown(root.left))
        rsum = max(0, self.maxPathDown(root.right))
        # 为了判断当前根节点得到的sum，是否最大
        cursum = root.val + lsum + rsum
        if cursum > self.max_sum:
            self.max_sum = cursum
        # 当前root向上返回值的时候，因为只能是当前root的一侧子树，所以只取最大的一侧。
        # 虽然加上root.val可能小于0，但是在上层node会max(0)
        return max(lsum, rsum) + root.val
