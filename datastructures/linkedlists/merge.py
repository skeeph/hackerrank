class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return "{data}".format(data=self.data)


def MergeLists(headA, headB):
    if headA is None:
        return headB
    elif headB is None:
        return headA
    head = None
    tail = None
    while True:
        if headA is None and headB is None:
            break

        if headA is None:
            curr = Node(headB.data)
            headB = headB.next
        elif headB is None:
            curr = Node(headA.data)
            headA = headA.next
        else:
            if headA.data <= headB.data:
                curr = Node(headA.data)
                headA = headA.next
            else:
                curr = Node(headB.data)
                headB = headB.next

        if head is None:
            head = curr
            tail = head
        else:
            tail.next = curr
            tail = curr
    return head


if __name__ == '__main__':
    a = Node(1, Node(2, Node(5)))
    b = Node(3, Node(4, Node(6, Node(7))))
    MergeLists(a, b)
