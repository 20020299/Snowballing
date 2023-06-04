class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def lca(root, n1, n2):
    if root is None:
        return None

    if root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)

    if root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)

    return root


def main():
    tree = Node(6)
    tree.left = Node(2)
    tree.right = Node(8)
    tree.left.left = Node(0)
    tree.left.right = Node(4)
    tree.left.right.left = Node(3)
    tree.left.right.right = Node(5)
    tree.right.left = Node(7)
    tree.right.right = Node(9)

    p = 2
    q = 8
    ans = lca(tree, p, q)
    print(ans.data)


if __name__ == "__main__":
    main()
