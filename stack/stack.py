


class ArrayStack(object):


    def __init__(self, sz):
        self.sz = sz
        self.ptr = 0
        self.items = [0 for i in range(sz)]
    
    
    def push(self, val):
        if self.ptr == self.sz:
            return False
        self.items[self.ptr] = val
        self.ptr += 1
        return True


    def pop(self):
        if self.ptr == 0:
            return None
        self.ptr -= 1
        return self.items[self.ptr]

    def top(self):
        if self.ptr == 0:
            return None
        return self.items[self.ptr - 1]


class Node(object):


    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkTableStack(object):
    

    def __init__(self):
        self._top = None
        
    def push(self, val):
        val_node = Node(val)
        val_node.next = self._top
        self._top = val_node

    def pop(self):
        if self._top is None:
            return None
        val = self._top.val
        self._top = self._top.next
        return val

    def top(self):
        if self._top is None:
            return None
        return self._top.val




if __name__ == '__main__':
    lt_st = LinkTableStack()
    [lt_st.push(i) for i in range(0, 5)]
    print(lt_st.pop())
    print(lt_st.top())

