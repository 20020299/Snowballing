class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Height:
    def __init__(self):
        self.height = 0


def isHeightBalanced(root, height):
    left_height = Height()
    right_height = Height()

    if root is None:
        return True

    l = isHeightBalanced(root.left, left_height)
    r = isHeightBalanced(root.right, right_height)

    height.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False


def main():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(2)
    tree.right.left = Node(3)
    tree.right.right = Node(3)
    tree.right.right.left = Node(4)
    tree.right.right.right = Node(4)

    height = Height()

    print(isHeightBalanced(tree, height))


if __name__ == "__main__":
    main()
