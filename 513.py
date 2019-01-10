# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.t = {}
        
        def dfs(node, depth):
            if node:
                if depth not in self.t:
                    self.t[depth] = node.val
                if node.left:
                    dfs(node.left, depth+1)
                if node.right:
                    dfs(node.right, depth+1)
        
        dfs(root, 0)
        if not self.t:
            return None
        m = max(self.t.keys())
        return self.t[m]
 
 # 看了另外一个人的答案，也可以不用dict，
 # 因为是preorder，直接keep 一个 max——depth即可
