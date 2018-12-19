# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans, i = [], 0
        que1, que2 = [root], []
        while que1 or que2:
            tmp = []
            if i % 2 == 0:
                for p in que1:
                    tmp.append(p.val)
                for p in que1[::-1]:
                    
                    if p.right:
                        que2.append(p.right)
                    if p.left:
                        que2.append(p.left)
                que1 = []
            else:
                for p in que2:
                    tmp.append(p.val)
                for p in que2[::-1]:
                    if p.left:
                        que1.append(p.left)
                    if p.right:
                        que1.append(p.right)
                que2 = []
            i += 1
            ans.append(tmp)
                        
        
        return ans
                
        
        
