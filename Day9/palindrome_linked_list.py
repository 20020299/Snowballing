class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode


def isPalindrome(head):
    tmp = head
    stack = []
    isPalin = True

    while tmp is not None:
        stack.append(tmp.val)
        tmp = tmp.next

    while head is not None:
        i = stack.pop()
        if head.data == i:
            isPalin = True
        else:
            isPalin = False
            break
        head = head.ptr

    return isPalin
