# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = dict()
        self.preorder(root, count)
        if not count:
            return []
        
        fre = max(count.values())
        return [k for k, v in count.items() if v == fre]
        
    def preorder(self, node, count):
        if node:
            if node.val not in count:
                count[node.val] = 1
            else:
                count[node.val] += 1
                
            if node.left:
                self.preorder(node.left, count)
            if node.right:
                self.preorder(node.right, count)
