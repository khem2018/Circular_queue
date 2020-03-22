
# coding: utf-8

# In[120]:


class Circular_queue:  
    class _Node:
        def __init__(self, data, pre=None, nxt=None):
            self._data = data
            self._pre= pre
            self._nxt = nxt     
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0  
    
    def enqueue(self, data):
        new_node = self._Node(data=data)
        if not self._head:
            self._head = new_node
            self._tail = new_node
        else:
            temp = self._head
            self._head = new_node
            self._head._nxt= temp
            temp._pre=self._head
            self._tail._nxt = self._head  
        self._size +=1
        print('Element inserted: {0}'.format(self._head._data))

    def dequeue_from_front(self):
        rep = self._head
        self._head = self._head._nxt
        self._head._pre = None
        self._size -=1
        print('Element removed: {0}'.format(rep._data))
    
    def dqueue_from_end(self):
        rep = self._tail
        self._tail = self._tail._pre
        self._tail._nxt = self._head
        self._size -=1
        print('Element removed: {0}'.format(rep._data))
    
    def get_size(self):
        return self._size
    
    def print_queue(self):
        initial_pointer = self._head
        counter = 0
        while counter <=self._size:
            print(initial_pointer._data)
            print('Circular_queue: {}'.format(initial_pointer._data))
            initial_pointer = initial_pointer._nxt
            counter+=1
