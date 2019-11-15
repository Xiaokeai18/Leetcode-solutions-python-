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
        pre = ListNode(0)
        pre.next = head
        left,right = pre,pre
        for i in range(n):
            right = right.next
        while(right.next):
            right = right.next
            left = left.next
        left.next = left.next.next
        return pre.next
        