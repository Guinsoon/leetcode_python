# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return
        l = 0
        node = head
        while node:
            node = node.next
            l += 1
        cur = head
        if l == n:
            return head.next
        for _ in range(l - n - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = node1.next = ListNode(2)
    node3 = node2.next = ListNode(3)
    node4 = node3.next = ListNode(4)
    node5 = node4.next = ListNode(5)
    print(Solution().removeNthFromEnd(node1, 2))


