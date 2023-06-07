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

    def getLen(self):
        tmp = self.head
        len = 0

        while tmp is not None:
            len += 1
            tmp = tmp.next

        return len

    def printMiddle(self):
        if self.head is not None:
            len = self.getLen()
            tmp = self.head

            midIdx = len // 2
            while midIdx != 0:
                tmp = tmp.next
                midIdx -= 1

            print(tmp.val)


def main():
    list1 = LinkedList()
    list1.head = Node(1)
    a2 = Node(2)
    a3 = Node(3)
    a4 = Node(4)
    a5 = Node(5)
    a6 = Node(6)
    list1.head.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a5
    a5.next = a6

    list1.printMiddle()


if __name__ == "__main__":
    main()