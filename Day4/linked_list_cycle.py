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


def detectLoop(llist):
    s = set()
    temp = llist.head
    while temp:
        if temp in s:
            return True
        s.add(temp)

        temp = temp.next

    return False


def main():
    list1 = LinkedList()
    list1.head = Node(3)
    a2 = Node(2)
    a3 = Node(0)
    a4 = Node(4)
    list1.head.next = a2
    a2.next = a3
    a3.next = a4
    a4.next = a2

    print(detectLoop(list1))


if __name__ == "__main__":
    main()
