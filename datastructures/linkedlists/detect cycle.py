class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return "{data}".format(data=self.data)


def has_cycle(head: Node):
    T = {}
    while head != None:
        if head not in T.keys():
            T[head] = 1
        else:
            return 1
        head = head.next
    return 0
