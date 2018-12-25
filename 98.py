class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        nums = []
        def inorder(node):
            if node:                
                if node.left:
                    inorder(node.left)
                nums.append(node.val)
                if node.right:
                    inorder(node.right)
        
        inorder(root)
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        st, pre = [], []     # python不能像c那样引用，只能构建数组使用pre
        p = root
        while st or p:
            while p:
                st.append(p)
                p = p.left
    
            p = st.pop()
            if pre and pre[-1] >= p.val:
                return False
            pre.append(p.val)
            
            p = p.right # 让p指向当前节点的右，如果右侧None，那么会出栈一个；否则，会入栈。
        return True
        return True
        return True
