class Solution(object):
    def kthSmallest(self, root, k):
        # this is the most slow way, inorder and then select
        ans = []
        
        def inorder(root, ans):
            if root:
                inorder(root.left, ans)
                ans.append(root.val)
                inorder(root.right, ans)
                
        inorder(root, ans)
        return ans[k-1]
        
    def kthSmallest2(self, root, k):
        self.k = k
        self.ans = None
        self.helper(root)
        return self.ans
        
    def helper(self, node):
        if not node:
            return
        self.helper(node.left) # 如果node非null
        self.k -= 1
        if self.k == 0:
            self.ans = node.val
            return
        self.helper(node.right)
        
