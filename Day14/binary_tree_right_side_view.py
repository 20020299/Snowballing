from collections import deque


class Node:
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


def rightView(root):
    if root is None:
        return

    q = deque()
    q.append(root)

    while q:
        n = len(q)

        while n > 0:
            n -= 1
            node = q.popleft()

            if n == 0:
                print(node.data, end=" ")

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
