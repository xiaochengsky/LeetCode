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
        if head.next.next is None:
            if head.val == head.next.val:
                return None

        p = ListNode(0)
        phead = p
        p.next = head
        cur = head
        while cur and cur.next:
            # 初始化的时a指向的是哑结点，所以比较逻辑应该是a的下一个节点和b的下一个节点
            if p.next.val != cur.next.val:
                p = p.next
                cur = cur.next
            else:
                # 如果a、b指向的节点值相等，就不断移动b，直到a、b指向的值不相等
                while cur and cur.next and p.next.val == cur.next.val:
                    cur = cur.next
                p.next = cur.next
                cur = cur.next

        return phead.next
