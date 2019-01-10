# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        ans, stack = [], [root]
        while stack:
            tmp_stack, level = [], []
            for node in stack:
                level.append(node.val)
                if node.left:
                    tmp_stack.append(node.left)
                if node.right:
                    tmp_stack.append(node.right)
            ans.append(max(level))
            stack = tmp_stack
        
        return ans
