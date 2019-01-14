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
        head = tail = TreeLinkNode(0)
        while root:
            for c in (root.left, root.right):
                tail.next = c
                if c:
                    tail = tail.next
                else:
                    break
            if root.next:
                root = root.next
            else:
                root = head.next
                tail = head
    
    # 另外一种方案，利用了满二叉树的性质
    def connect(self, root):
        if not root:    return
        cur = root
        nex = root.left
        while cur.left:
            print(cur.val)
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = nex
                nex = cur.left
