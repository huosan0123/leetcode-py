# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        leng, p = 0, head
        while p:
            p = p.next
            leng += 1
        half1 = (leng-1) / 2 + (leng-1) % 2
        p, cnt, half2 = head.next, 0, None
        while p:
            
            cnt += 1
            if cnt == half1:
                half2 = p.next
                p.next = None         # 这里是要点，不然环状
                break
            p = p.next
        half2 = self.reverseList(half2)

        pre, q = head, half2
        while q != None:
            curp = pre
            pre = pre.next
            curq = q
            q = q.next
            curq.next = curp.next
            curp.next = curq
        
        
    def reverseList(self, head):
        if not head:
            return head
        
        tmp = ListNode(-1)
        tmp.next = head
        p = head.next
        tmp.next.next = None
        while p:
            cur = p
            p = p.next
            cur.next = tmp.next
            tmp.next = cur
        return tmp.next
