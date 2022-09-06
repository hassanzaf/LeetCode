class Node:
    def __init__(self, elm, prv, nxt):
        self.elm = elm
        self.prv = prv
        self.nxt = nxt

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def push_front(self, elm):
        if self.head is None:
            node = Node(elm, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(elm, None, self.head)
            self.head.prv = node
            self.head = node

    def pop_front(self):
        node = self.head
        if node.nxt is None:
            self.head = None
            self.tail = None
        else:
            self.head = node.nxt
            self.head.prv = None
        return node.elm

    def push_back(self, elm):
        if self.head is None:
            node = Node(elm, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(elm, self.tail, None)
            self.tail.nxt = node
            self.tail = node

    def pop_back(self):
        node = self.tail
        if node.prv is None:
            self.head = None
            self.tail = None
        else:
            self.tail = node.prv
            self.tail.nxt = None
        return node.elm

