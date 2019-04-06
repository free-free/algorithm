



class ArrayQueue(object):

    
    def __init__(self, sz:int)->None:
        self._sz = sz
        self._queue = [0 for i in range(self._sz)]
        self._head = 0
        self._tail = 0


    def enqueue(self, val)->bool:
        if self._tail == self._sz:
            if self._head == 0:
                # stack is empty
                return False
            for i in range(self._head, self._tail):
                self._queue[i - self._head] = self._queue[i]
                self._queue[i] = 0
            self._tail = self._tail - self._head
            self._head = 0
        self._queue[self._tail] = val
        self._tail += 1
        return True

    def dequeue(self):
        if self._head == self._tail:
            return None
        val = self._queue[self._head]
        self._queue[self._head] = 0
        self._head += 1
        return val


class Node(object):

    
    def __init__(self, val=None)->None:
        self.val = val
        self.next = None


class LnkTblQueue(object):


    def __init__(self)->None:
        self._head = Node()
        self._tail = self._head


    def enqueue(self, val):
        new_node = Node(val)
        self._tail.next = new_node
        self._tail = new_node
        return True

    def dequeue(self):
        if self._head == self._tail or self._head.next is None:
            return None
        val = self._head.next.val
        self._head.next = self._head.next.next
        return val


class ArrayCircularQueue(object):


    def __init__(self, sz:int=10)->None:
        self._sz = sz
        self._head, self._tail = 0,0
        self._queue = [0 for i in range(sz)]

    def enqueue(self, val):
        if (self._tail + 1) % self._sz == self._head:
            return False
        self._queue[self._tail] = val
        self._tail = (self._tail + 1) % self._sz
        return True

    def dequeue(self):
        if self._tail == self._head:
            return None
        val = self._queue[self._head]
        self._head = (self._head + 1) % self._sz
        return val


if __name__ == '__main__':
    ArrayQueue(21)
