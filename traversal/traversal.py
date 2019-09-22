class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Traversal:
    def bfs(self, root):
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def dfs(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        return res


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

    print(Traversal().bfs(node1))
    print(Traversal().dfs(node1, []))

