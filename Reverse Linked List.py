class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseLinkedList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            temp = pHead.next
            pHead.next = last
            last = pHead
            pHead = temp
        return last


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node = node1
    while node:
        print(node.val)
        node = node.next
    print(20 * '-')
    new_node = Solution().reverseLinkedList(node1)
    while new_node:
        print(new_node.val)
        new_node = new_node.next
