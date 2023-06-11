class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


def sortedArrayToBST(arr):
    if not arr:
        return None

    mid = (len(arr)) // 2
    root = Node(arr[mid])
    root.left = sortedArrayToBST(arr[:mid])
    root.right = sortedArrayToBST(arr[mid + 1:])

    return root

