class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

    def __str__(self):
        return "Node: {data}, next={n}, prev={p}".format(data=self.data, n=self.next.data, p=self.prev.data)


def Reverse(head):
    p = head.next
    while p is not None:
        temp = head.prev
        head.prev = head.next
        head.next = temp
        head = p
        p = p.next
    temp = head.prev
    head.prev = head.next
    head.next = temp
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
