class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class PreOrder:
    def pre_order(self, root):
        if not root:
            return
        print(root.val)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def pre_order2(self, root):
        if not root:
            return
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)

    def pre_order_stack(self, root):
        if not root:
            return []
        res = [root.val]
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
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

    print(PreOrder().pre_order(node1))
    print(PreOrder().pre_order2(node1))
    print(PreOrder().pre_order_stack(node1))
