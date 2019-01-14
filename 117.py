# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        st = [root]
        while st:
            n, tmp = len(st), []
            for node in st:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            for i in range(n-1):
                st[i].next = st[i+1]
            st = tmp

    def connect(self, root):
        # python 里head 和tail实际上指向同一个对象
        # 把level当作有head的链表处理
        head = tail = TreeLinkNode(0)
        while root:
            for node in (root.left, root.right):
                tail.next = node
                if node:
                    tail = tail.next
            
            # 获得下一个需要处理的node
            if root.next:
                root = root.next
            else:       # 这一层处理结束，处理下一层
                # root需要指向下一层的第一个，同时把tail指向head，重新利用该头指针
                root, tail = head.next, head 
