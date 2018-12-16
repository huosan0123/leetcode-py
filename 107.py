# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if not root:
            return ans
        que1, que2 = [root], []
        while que1 or que2:
            if len(que1) > 0:
                tmp = []
                for p in que1:
                    tmp.append(p.val)
                    if p.left:
                        que2.append(p.left)
                    if p.right:
                        que2.append(p.right)
                ans.append(tmp[::])
                que1 = []
            else:
                tmp = []
                for p in que2:
                    tmp.append(p.val)
                    if p.left:
                        que1.append(p.left)
                    if p.right:
                        que1.append(p.right)
                ans.append(tmp[::])
                que2 = []
        return ans[::-1]
                
