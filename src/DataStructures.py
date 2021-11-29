##########################################
############## STACKS AND QUEUES
##########################################

class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def enqueue(self, data):
        self.q.append(data)

    def dequeue(self):
        if self.is_empty():
            return
        item = self.q[0]
        self.q = self.q[1:]
        return item

    def peek(self):
        if self.is_empty():
            return
        return self.q[0]

    def length(self):
        return len(self.q)

class Stack:
    def __init__(self):
        self.s = []

    def push(self, data):
        self.s.append(data)
        return

    def pop(self):
        if len(self.s) == 0:
            return None
        last = self.s[-1]
        self.s = self.s[:-1]
        return last

    def peek(self):
        return None if len(self.s) == 0 else self.s[-1]

    def is_empty(self):
        return len(self.s) == 0

class QueueTwoStacks:
    def __init__(self):
        self.s1 = Stack() # newest on top
        self.s2 = Stack() # oldest on top

    def is_empty(self):
        return self.s1.is_empty() & self.s2.is_empty()

    def enqueue(self, data):
        self.s1.push(data)
        return

    def dequeue(self):
        if self.is_empty():
            return None

        # move everything from s1 to s2 if s2 is empty
        if self.s2.is_empty():
            while not self.s1.is_empty():
                elt = self.s1.pop()
                self.s2.push(elt)

        # pop off s2
        dequeued = self.s2.pop()

        return dequeued

    def peek(self):
        if self.is_empty():
            return None

       # move everything from s1 to s2 if s2 is empty
        if self.s2.is_empty():
            while not self.s1.is_empty():
                elt = self.s1.pop()
                self.s2.push(elt)

        # pop off s2
        peeked = self.s2.peek()

        return peeked

class StackTwoQueues:
    """
    Induction hypothesis: q1 is in stack order, q2 is empty
    """
    def __init__(self):
        self.q1 = Queue() # loaded
        self.q2 = Queue() # backup

    def is_empty(self):
        return self.q1.is_empty() & self.q2.is_empty()

    def push(self, data):
        self.q2.enqueue(data)
        while not self.q1.is_empty():
            temp = self.q1.dequeue()
            self.q2.enqueue(temp)

        # reassign to preserve IH
        temp = self.q2
        self.q2 = Queue()
        self.q1 = temp

    def pop(self):
        return self.q1.dequeue()

    def peek(self):
        return self.q1.peek()

class StackTwoQueuesV2:
    """
    Induction hypothesis: q1 is in queue order, q2 is empty
    """
    def __init__(self):
        self.q1 = Queue() # loaded
        self.q2 = Queue() # backup

    def is_empty(self):
        return self.q1.is_empty() & self.q2.is_empty()

    def push(self, data):
        self.q1.enqueue(data)

    def pop(self):
        if self.q1.is_empty():
            return

        # shuffle everything into backup queue except last elt
        while self.q1.length() > 1:
            temp = self.q1.dequeue()
            self.q2.enqueue(temp)

        # grab the pop
        data = self.q1.dequeue()

        # reassign to preserve IH
        temp = self.q2
        self.q2 = Queue()
        self.q1 = temp
        return data

    def peek(self):
        if self.q1.is_empty():
            return

        # shuffle everything into backup queue except last elt
        while self.q1.length() > 1:
            temp = self.q1.dequeue()
            self.q2.enqueue(temp)

        # grab the peek and put it back
        data = self.q1.dequeue()
        self.q2.enqueue(data)

        # reassign to preserve IH
        temp = self.q2
        self.q2 = Queue()
        self.q1 = temp
        return data

##########################################
############## LINKED LISTS
##########################################

class SinglyLinkedListNode:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        """
        Insert at the end.
        """
        # edge case: list was empty
        if self.length == 0:
            self.head = SinglyLinkedListNode(data, None)
            self.length += 1
            return

        # retrieve next node until end is reached
        cur_node = self.head
        for _ in range(self.length - 1):
            cur_node = cur_node.next

        # insert after last node is reached
        cur_node.next = SinglyLinkedListNode(data, None)
        self.length += 1

    def insert_at_position(self, data, n: int):
        """
        Insert at position n. Assume 0-index.
        """
        assert (n >= 0) & (n <= self.length)

        if n == 0:
            new_node = SinglyLinkedListNode(data, self.head)
            self.head = new_node
            self.length += 1
            return
        elif n == self.length:
            self.insert(data)
            return

        # retrieve node right before position n
        cur_node = self.head
        for _ in range(n - 1):
            cur_node = cur_node.next

        # swap
        new_node = SinglyLinkedListNode(data, cur_node.next)
        cur_node.next = new_node
        self.length += 1
        return

    def delete(self):
        """
        Delete last node.
        """
        if self.length == 0:
            return
        elif self.length == 1:
            self.head = None
            self.length -= 1
            return

        # retrieve next-to-last node
        cur_node = self.head
        for _ in range(self.length - 1):
            cur_node = cur_node.next

        # remove the pointer to the last node
        cur_node.next = None
        self.length -= 1
        return

    def delete_at_position(self, n):
        """
        Delete node at position n. Assume 0-index.
        """
        assert (n >= 0) & ((n < self.length) | (self.length == 0))

        # edge cases
        if self.length == 0:
            # nothing to delete
            return
        elif n == 0:
            # delete head
            self.head = self.head.next
            self.length -= 1
            return
        elif n == self.length - 1:
            # tail delete already implemented
            self.delete()
            return

        # skip n
        cur_node = self.head
        for _ in range(n - 1):
            cur_node = cur_node.next
        cur_node.next = cur_node.next.next
        self.length -= 1
        return

    def print_data(self):
        """
        For debugging purposes: print data in order.
        """
        if self.length == 0:
            return
        cur_node = self.head
        print(str(cur_node.data) + "\n")
        for _ in range(self.length - 1):
            cur_node = cur_node.next
            print(str(cur_node.data) + "\n")

class DoublyLinkedListNode:
    def __init__(self, data, next_node, prev_node):
        self.data = data
        self.next = next_node
        self.prev = prev_node

# TODO: implement
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
