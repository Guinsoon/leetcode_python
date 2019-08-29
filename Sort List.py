# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        prev = head
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = p = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                p = l1
                l1 = l1.next
            else:
                p.next = l2
                p = l2
                l2 = l2.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next
