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


def merge(list1, list2):
    ans = []
    head1 = list1.head
    head2 = list2.head
    while head1 is not None:
        ans.append(head1.val)
        head1 = head1.next

    while head2 is not None:
        ans.append(head2.val)
        head2 = head2.next

    ans.sort()
    return ans


def main():
    # List 1
    list1 = LinkedList()
    list1.head = Node(1)
    a2 = Node(2)
    a3 = Node(4)
    list1.head.next = a2
    a2.next = a3

    # List 2
    list2 = LinkedList()
    list2.head = Node(1)
    b2 = Node(3)
    b3 = Node(4)
    list2.head.next = b2
    b2.next = b3be

    print(merge(list1, list2))


if __name__ == "__main__":
    main()
