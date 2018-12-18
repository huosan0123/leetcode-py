# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        ans = []
        
        def dfs(node, path, c):
            if not node.left and not node.right:
                if (c - node.val) == 0:
                    ans.append(path+[node.val])
                    return
            c -= node.val
            if node.left:
                dfs(node.left, path + [node.val], c)
            if node.right:
                dfs(node.right, path+[node.val], c)
        dfs(root, [], sum)
        return ans
        
