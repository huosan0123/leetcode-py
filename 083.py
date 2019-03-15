# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p, cur = head, head.next
        while cur:
            if p.val != cur.val:
                p.next = cur
                p = p.next
            cur = cur.next
        p.next = None   # 最后的那个节点要单独处理。
        return head
        
