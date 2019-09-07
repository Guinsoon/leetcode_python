# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        view = []
        self.right_view(root, view, 0)
        return view

    def right_view(self, node, result, depth):
        if not node:
            return
        if len(result) == depth:
            result.append(node.val)
        self.right_view(node.right, result, depth+1)
        self.right_view(node.left, result, depth+1)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node3.right = node5

    print(Solution().rightSideView(node1))
