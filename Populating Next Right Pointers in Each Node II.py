# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return
        node = root
        while node:
            temp = Node(0, None, None, None)
            cur = temp
            while node:
                if node.left:
                    cur.next = node.left
                    cur = cur.next
                if node.right:
                    cur.next = node.right
                    cur = cur.next
                node = node.next
            node = temp.next
        return root


if __name__ == "__main__":
    node1 = Node(1, None, None, None)
    node2 = Node(2, None, None, None)
    node3 = Node(3, None, None, None)

    node1.left = node2
    node1.right = node3
    Solution().connect(node1)

