# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        n = len(inorder)
        root = self.buildCore(inorder, 0, n-1, postorder, 0, n-1)
        return root
    
    def buildCore(self, inorder, inlow, inhigh, postorder, plow, phigh):
        if inlow > inhigh:
            return None
        elif inlow == inhigh:
            node = TreeNode(inorder[inlow])
            return node
        val = postorder[phigh]
        for i in range(inlow, inhigh+1):
            if inorder[i] == val:
                break
        root = TreeNode(val)
        left_len = i - inlow
        root.left = self.buildCore(inorder, inlow, i-1, postorder, plow, plow + left_len - 1)
        root.right = self.buildCore(inorder, i+1, inhigh, postorder, plow + left_len, phigh-1)
        return root
