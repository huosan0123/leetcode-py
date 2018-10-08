# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans, stk = [], []
        stk.append(root)
        while stk:
            p = stk.pop()
            if p:
                ans.append(p.val)
                stk.append(p.right)
                stk.append(p.left)
        return ans
        
    def preorderTraversal(self, root):
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
