# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # node, depth, pos
        # very clean code. 膜！！把pos设置为0，那每层都是从0开始，很棒
        que = [(root, 0, 0)]
        curdep = ans = left = 0
        for node, dep, pos in que:
            if node:
                que.append((node.left, dep+1, pos*2))
                que.append((node.right, dep+1, pos*2+1))
                if curdep != dep:  # 进入新的一层了
                    curdep = dep
                    left = pos
                ans = max(pos - left + 1, ans)
        return ans
