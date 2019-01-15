# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        我用的和BST那道题一样的解法。就是dfs这里需要注意。如何保证退栈没问题
        """
        def dfs(node, path, a):
            if node:
                path.append(node)
                if node.val == a.val:
                    return True
                if dfs(node.left, path, a):
                    return True
                if dfs(node.right, path, a):
                    return True
                path.pop()
        path1, path2 = [], []
        dfs(root, path1, p)
        dfs(root, path2, q)
        
        m, n, i = len(path1), len(path2), 0
        while i < m and i < n:
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]
