class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def PrintTree(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PrintTree(root.left)
            res = res + self.PrintTree(root.right)
        return res


def invertTree(root):
    if not root:
        return
    stack = [root]

    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root


def main():
    tree = Node(4)
    tree.left = Node(2)
    tree.right = Node(7)
    tree.left.left = Node(1)
    tree.left.right = Node(3)
    tree.right.left = Node(6)
    tree.right.right = Node(9)
    print(tree.PrintTree(tree))

    ans = invertTree(tree)
    print(ans.PrintTree(ans))


if __name__ == "__main__":
    main()
