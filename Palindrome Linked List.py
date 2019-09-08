# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        if not head:
            return True
        l = 0
        node = head
        while node:
            l += 1
            node = node.next

        cur = head
        half = l // 2
        while half > 1:
            cur = cur.next
            half -= 1
        new_head = cur.next

        cur.next = None
        last = None
        while new_head:
            temp = new_head.next
            new_head.next = last
            last = new_head
            new_head = temp
        half = l // 2
        while half > 0:
            if last.val != head.val:
                return False
            last = last.next
            head = head.next
            half -= 1
        return True

    def isPalindrome2(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        last = None
        while slow:
            temp = slow.next
            slow.next = last
            last = slow
            slow = temp
        while last:
            if head.val != last.val:
                return False
            head = head.next
            last = last.next

        return True



if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(1)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print(Solution().isPalindrome(node1))
