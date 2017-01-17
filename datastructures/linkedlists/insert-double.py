class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return "Node: {data}, next={n}, prev={p}".format(data=self.data, n=self.next.data, p=self.prev.data)


def SortedInsert(head, data):
    if head.data > data:
        n = Node(data=data, next_node=head)
        head.prev = n
        head = n
        return head

    c = head
    while c.next is not None:
        if c.data < data < c.next.data:
            n = Node(data=data, next_node=c.next, prev_node=c)
            if c.next is not None:
                c.next.prev = n
            c.next = n
            return head
        c = c.next

    n = Node(data=data, prev_node=c)
    c.next = n
    return head


if __name__ == '__main__':
    a = Node(0)
    b = Node(1)
    c = Node(1)
    d = Node(3)
    a.prev = None
    a.next = b
    b.prev = a
    b.next = c
    c.prev = b
    c.next = d
    d.prev = c
    d.next = None
    res = SortedInsert(a, 2)
    print(res)
