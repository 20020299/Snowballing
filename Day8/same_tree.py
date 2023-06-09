class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sameTree(a, b):
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return ((a.data == b.data) and
                sameTree(a.left, b.left) and
                sameTree(a.right, b.right))

    return False


