class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return "{data}".format(data=self.data)


def GetNode(head: Node, position: int) -> int:
    v = []
    while head is not None:
        v.append(head.data)
        head = head.next
    return v[-position - 1]


if __name__ == '__main__':
    a = Node(1, Node(2, Node(3, Node(4))))

    print()
