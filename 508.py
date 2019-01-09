# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.ht = {}
        
        def dfs(node):
            # 弄的这么复杂，是担心如果node=none, 0的时候的如何处理。
            # 不应该给None产生的 0 设置 key=0的。
            if node:
                left_sum = dfs(node.left)
                right_sum = dfs(node.right)
                if left_sum and right_sum:
                    s = left_sum + right_sum + node.val
                elif left_sum or right_sum:
                    s = (left_sum or right_sum) + node.val
                else:
                    s = node.val
                if s not in self.ht:
                    self.ht[s] = 1
                else:
                    self.ht[s] += 1
                return s
        
        dfs(root)
        most_freq = max(self.ht.values())
        return [k for k, v in self.ht.items() if v == most_freq]
        
   def findFrequentTreeSum(self, root):
        if root == None: return []

        def getSum(node):  # 这里None直接返回0，不设置key，所以完美。
            if node == None: return 0
            s = node.val + getSum(node.left) + getSum(node.right)
            c[s] += 1      # Counter可以直接加
            return s

        c = collections.Counter()
        getSum(root)
        frequent = max(c.values())
        return [s for s in c if c[s] == frequent]
