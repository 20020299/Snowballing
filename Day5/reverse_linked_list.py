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

    def print(self):
        p = self.head
        while p.next:
            print(p.val)
            p = p.next


def reverse(llist):
    stack = []
    start = llist.head
    while start is not None:
        stack.append(start.val)
        start = start.next
    newLlist = LinkedList()
    while len(stack) != 0:
        newLlist.add(stack.pop())
    return newLlist.print()


def main():
    list1 = LinkedList()
    list1.head = Node(3)
    a2 = Node(2)
    a3 = Node(0)
    a4 = Node(4)
    list1.head.next = a2
    a2.next = a3
    a3.next = a4

    print(reverse(list1))


if __name__ == "__main__":
    main()
