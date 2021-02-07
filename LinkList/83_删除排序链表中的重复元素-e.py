# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        pre = head
        cur = head.next
        while cur:
            if pre.val == cur.val:
                # pre.next = cur.next
                cur = cur.next
            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        pre.next = None
        return head
