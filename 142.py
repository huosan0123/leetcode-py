# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break
        else:        # while 居然能搭配else，才发现啊
            return None
        
        pt1, pt2 = head, p1    # 这里p1 p2都可以
        while (pt1 != pt2):
            pt1 = pt1.next
            pt2 = pt2.next
        return pt1
