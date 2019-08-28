class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class LevelOrder:
    def level_order(self, root):
        res = []
        self.dfs(res, root, 0)
        return res

    def dfs(self, res, root, level):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        self.dfs(res, root.left, level+1)
        self.dfs(res, root.right, level+1)


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)

    node1.left = node2
    node1.right = node3

    node2.left = node4
    node2.right = node5
    node3.right = node6

    node5.left = node7
    node5.right = node8

    print(LevelOrder().level_order(node1))

