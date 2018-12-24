# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        st, pre = [root], None
        while st:
            node = st.pop()
            if pre:
                pre.right = node
                pre.left = None
            pre = node
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
