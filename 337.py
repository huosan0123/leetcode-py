# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
        if not root:
            return 0
        
        dd = {}
        def dfs(root):
            if not root:
                return 0
            if root in dd:  return dd[root]
            
            val = root.val
            if root.left:
                val += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                val += dfs(root.right.left) + dfs(root.right.right)
            
            ans = max(val, dfs(root.left) + dfs(root.right))
            dd[root] = ans
            return ans
        
        return dfs(root)
