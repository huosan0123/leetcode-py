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
