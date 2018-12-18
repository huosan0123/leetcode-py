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
        
    def pathSum(self, root, sum):
        """
        改动一小部分，就超过100%，简直666啊
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
                    ans.append(path+[node.val])   # 这里符合路径，直接复制数组
                    return
            c -= node.val
            path.append(node.val)     # 因为复制数组耗时，所以更改为只在必要的时候复制。
            if node.left:
                dfs(node.left, path, c)
            if node.right:
                dfs(node.right, path, c)
            path.pop()                 # 退站的时候，取出放入的节点
        dfs(root, [], sum)
        return ans
