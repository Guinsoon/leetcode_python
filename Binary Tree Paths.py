# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        # self.helper(root, res, [])
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        # if not root.left and not root.right:
        #     ls.append(root.val)
        #     res.append(ls[:])
        # if root.left:
        #     ls.append(root.val)
        #     self.dfs(root.left, ls, res)
        # if root.right:
        #     ls.append(root.val)
        #     self.dfs(root.right, ls, res)

        if not root.left and not root.right:
            res.append(ls + str(root.val))
        if root.left:
            self.dfs(root.left, ls + str(root.val) + "->", res)
        if root.right:
            self.dfs(root.right, ls + str(root.val) + "->", res)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node5 = TreeNode(5)

    node1.left = node2
    node1.right = node3

    node2.right = node5

    print(Solution().binaryTreePaths(node1))

