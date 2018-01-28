# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)  # using a head node
        p = head
        while(l1 != None and l2 != None):
            if (l1.val <= l2.val):
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next       # don't forget to update p
        while(l1 != None):   # could be simplified
            p.next = l1
            l1 = l1.next
            p = p.next
        while(l2 != None):
            p.next = l2
            l2 = l2.next
            p = p.next
        # p.next = l1 if l1 else p.next = l2
        return head.next
        
