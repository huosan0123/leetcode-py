# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.best = 0
        
        def height(node):
            if not node:
                return 0
            else:
                lh = height(node.left)
                rh = height(node.right)
                self.best = max(self.best, lh + rh)
                return max(lh, rh) + 1
                
        height(root)
        return self.best
