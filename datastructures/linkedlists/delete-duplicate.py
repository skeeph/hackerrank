class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return "{data}".format(data=self.data)


def RemoveDuplicates(head):
    c = head.next
    prev = head
    while c is not None:
        if c.data == prev.data:
            prev.next = c.next
            c = c.next
        else:
            prev = c
            c = c.next
    return head

if __name__ == '__main__':
    a = Node(1, Node(1, Node(2, Node(3, Node(4, Node(4))))))
    RemoveDuplicates(a)