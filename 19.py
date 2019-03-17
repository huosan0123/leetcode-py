# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        lens, ahead = 0, head
        while ahead:
            lens += 1
            ahead = ahead.next
        if not head or lens < n:
            return None
        if lens == n:
            return head.next
        pre, ahead = None, head
        while ahead:
            n -= 1
            if pre:
                pre = pre.next
            if n == -1:
                pre = head
            ahead = ahead.next
        pre.next = pre.next.next
        return head
