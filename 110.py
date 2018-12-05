# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            lh = self.getHeight(root.left)
            rh = self.getHeight(root.right)
            if abs(lh - rh) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getHeight(self, root):
        if not root:
            return 0
        else:
            left_h = self.getHeight(root.left)
            right_h = self.getHeight(root.right)
            return max(left_h, right_h) + 1
