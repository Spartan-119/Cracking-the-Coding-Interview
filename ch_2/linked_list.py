class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values:
            for value in values:
                self.append(value)

    def __repr__(self):
        """
         __repr__ method: It's a good practice to implement the __repr__ method for
         better debugging and representation of the linked list object.
        """
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.val))
            current = current.next
        return "->".join(nodes)

    def append(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def remove(self, val):
        if not self.head:
            return

        if self.head.val == val:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return

        current = self.head
        while current.next:
            if current.next.val == val:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
            else:
                current = current.next