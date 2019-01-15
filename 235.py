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
        我的代码还是一如既往的丑与复杂。最开始没想到思路，后面自己想到了
        """  
        if not root or not p or not q:
            return None
        path1, path2 = [], []
        node = root
        while node:
            path1.append(node)
            if node.val == p.val:
                break
            elif node.val > p.val:
                node = node.left
            else:
                node = node.right
        node = root
        while node:
            path2.append(node)
            if node.val == q.val:
                break
            elif node.val > q.val:
                node = node.left
            else:
                node = node.right
        m, n, i = len(path1), len(path2), 0
        while i < m and i < n:
            if path1[i] != path2[i]:
                break
            i += 1
        return path1[i-1]
    
    # 因为题目描述是unique，所以下面这个充分利用了BST的性质。更快一些！！！
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q:
            return None
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
                
