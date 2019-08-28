# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root, val):
        if not root:
            return
        if root.val == val:
            return root
        if root and root.val > val:
            return self.searchBST(root.left, val)
        if root and root.val < val:
            return self.searchBST(root.right, val)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3

    node2.right = node4
    node3.left = node5

    print(node1)
    print(Solution().searchBST(node1, 3))

