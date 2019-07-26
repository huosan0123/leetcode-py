# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fack = p = ListNode(-1)
        p.next = head
        
        while p.next and p.next.next:
            a, b, c = p.next, p.next.next, p.next.next.next
            
            a.next = c
            b.next = a
            p.next = b
            p = a
            
        return fack.next
