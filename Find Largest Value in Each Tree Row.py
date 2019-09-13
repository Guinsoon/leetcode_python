# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root):
        if not root:
            return
        path = []
        self.dfs(root, path, 0)
        res = list(map(max, path))
        return res

    def dfs(self, root, res, level):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)

    def largestValues2(self, root):
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node5 = TreeNode(5)
    node4 = TreeNode(3)
    node9 = TreeNode(9)

    node1.left = node3
    node1.right = node2

    node3.left = node5
    node3.right = node4
    node2.right = node9

    print(Solution().largestValues2(node1))

