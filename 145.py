# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        https://blog.csdn.net/zgaoq/article/details/79089819
        # 对照上面和王道的代码写的
        """
        stack = []
        pcur, pLastVisit = root, None
        ans = []
        while (pcur or stack):
            if pcur:
                stack.append(pcur)
                pcur = pcur.left
            else:
                pcur = stack.pop()
                if (pcur.right == None or pcur.right == pLastVisit):
                    ans.append(pcur.val)
                    pLastVisit = pcur
                    pcur = None             # 这里需要重置 pcur
                else:
                    stack.append(pcur)      # 因为右子树还没访问，所以根节点再次放进去
                    pcur = pcur.right
        return ans
