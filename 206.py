# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        newhead = None
        pre = None
        while p:
            q = p.next
            if q == None:
                newhead = p
            p.next = pre
            pre = p
            p = q
        return newhead
