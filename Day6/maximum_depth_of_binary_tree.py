class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def maxDepth(root):
    if root is None:
        return 0

    leftDepth = maxDepth(root.left)
    rightDepth = maxDepth(root.right)

    if leftDepth > rightDepth:
        return leftDepth + 1
    else:
        return rightDepth + 1


def main():
    tree = Node(3)
    tree.left = Node(9)
    tree.right = Node(20)
    tree.right.left = Node(15)
    tree.right.right = Node(7)

    print(maxDepth(tree))


if __name__ == "__main__":
    main()
