# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head

        while cur:
            if cur.val != val:
                pre = pre.next
                cur = cur.next
            else:
                pre.next = cur.next
                cur = pre.next
        return dummy.next

    def removeElements2(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head

        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    node1 = ListNode(1)
    print(Solution().removeElements(node1, 2))

