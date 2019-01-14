# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.post(root, [0])
        return root
        
    def post(self, node, res):
        if node:
            self.post(node.right, res)
            node.val += res[0]
            res[0] = node.val
            self.post(node.left, res)
