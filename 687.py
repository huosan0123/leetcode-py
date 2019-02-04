# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 题目意思就要花时间理解，path可以不通过root，即把某个node当作root形成path。
        if not root:
            return 0
        self.longest = 0
        
        def dfs(node):
            if not node:
                return 0
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            # 这两行比较精髓吧。我的话，可能就把node num作为返回值，然后path = num-1
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len+1) if node.right and node.right.val == node.val else 0

            # 如果当前node作为root的path最长
            if self.longest < left + right:
                self.longest = left + right
            # 值返回最大的一侧，因为path不能是三叉的
            return max(left, right)
        
        dfs(root)
        return self.longest
