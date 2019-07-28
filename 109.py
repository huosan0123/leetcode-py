# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        p, arr = head, []
        while p:
            arr.append(p.val)
            p = p.next
        
        return self.toBST(arr, 0, len(arr)-1)
    
    def toBST(self, arr, low, high):
        if low > high:
            return None
        elif low == high:
            return TreeNode(arr[low])
        else:
            mid = (low + high) / 2
            node = TreeNode(arr[mid])
            node.left = self.toBST(arr, low, mid-1)
            node.right = self.toBST(arr, mid+1, high)
            return node
