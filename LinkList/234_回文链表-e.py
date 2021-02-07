# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        mid = self.find_half(head)
        reverse = self.reversed_list(mid.next)

        result = True
        front = head
        laster = reverse
        while result and laster:
            if front.val == laster.val:
                front = front.next
                laster = laster.next
            else:
                result = False
        # 还原链表
        self.reversed_list(reverse)
        return result

    def find_half(self, head):
        slow, fast = head, head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reversed_list(self, head):
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre