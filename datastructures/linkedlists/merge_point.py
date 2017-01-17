class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return "{data}".format(data=self.data)


def FindMergeNode(headA, headB):
    p1 = headA
    p2 = headB
    len1 = len2 = 0
    while p1:
        len1 += 1
        p1 = p1.next
    while p2:
        len2 += 1
        p2 = p2.next

    if len1 > len2:
        for i in range(len1 - len2):
            headA = headA.next
    else:
        for i in range(len2 - len1):
            headB = headB.next
    while headA and headB:
        if headA == headB:
            return headA.data
        headA = headA.next
        headB = headB.next
