'''
Leetcode 146. LRU Cache

Description:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
  Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity 
  from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
'''

'''
LRU means 'Least Recently Used", the algorithm discards the least recently used items first by keeping track of when the resource is used.
'''

'''
Hashmap + Double Linked List
Hashmap is used to simulate the stack, map resource key to DLinkedNode
Double Linked List is used to achieve O(1) to delete the tail node (which is the LRU resource) 
and O(1) to push the most recently used resource to the head.
'''

class DLinkedNode: 
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0 ### current size
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {}

    ### TC: O(1)
    def _moveToHead(self, node): 
        node.next.prev, node.prev.next = node.prev, node.next ### cut from the original position
        node.prev, node.next = self.head, self.head.next ### insert
        self.head.next.prev = node ### link
        self.head.next = node ### link

    ### TC: O(1)
    def _addToHead(self, node):
        node.prev, node.next = self.head, self.head.next ### insert
        self.head.next.prev = node ### link
        self.head.next = node ### link

    ### TC: O(1)
    def _delete(self):
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        node.prev, node.next = None, None ### C/C++ style
        del self.cache[node.key]

    ### TC: O(1)
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._moveToHead(node)
            return node.val
        else:
            return -1
    
    ### TC: O(1)
    def put(self, key, value):
        if key in self.cache:  ### important
            node = self.cache[key]
            node.val = value  ### update cache
            self._moveToHead(node)
        else:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self._addToHead(node)
            if self.size == self.capacity:
                self._delete()
            else:
                self.size += 1
            
