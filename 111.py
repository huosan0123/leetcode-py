# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = [99999999]   # 为何depth = 999999，就不能访问
        
        def preorder(node, dep):
            
            if node:
                dep += 1
                if node.left:
                    preorder(node.left, dep)
                if node.right:
                    preorder(node.right, dep)
                if (not node.left) and (not node.right) and dep < depth[0]:
                    depth[0] = dep
            
        preorder(root, 0)
        return depth[0]
