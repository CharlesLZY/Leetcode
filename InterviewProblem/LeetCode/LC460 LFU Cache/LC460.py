'''
Leetcode 460. LFU Cache

Description:
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. 
When the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new item. 
For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. 
The key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). 
The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
'''

'''
LRU cache is easier to implement.
LRU means 'Least Recently Used", the algorithm discards the least recently used items first by keeping track of when the resource is used.

Hashmap + Double Linked List
Hashmap is used to simulate the stack, map resource key to DLinkedNode
Double Linked List is used to achieve O(1) to delete the tail node (which is the LRU resource) 
and O(1) to push the most recently used resource to the head.
The following helper function need to be implemented: 
_moveToHead(node)
_addToHead(node)
_deleteTail(node)
'''

'''
When two nodes have the same freq, we need to perform LRU rule.
So we can maintain some freq lists (at most C freq lists) to store nodes with the same freq.
Use double linked list to achieve LRU cache. Check the freq list have the highest freq to achieve LFU.

Hash Table: {key : DLinkedNode}
freq Table: {freq: DlinkedList}
'''
### Hash Table + Double Linked Lists
### TC: O(1) SC: O(C) where C is the capacity of the cache
class DLinkedNode: 
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self, freq):
        self.freq = freq
        self.length = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self, node):
        node.next.prev, node.prev.next = node.prev, node.next ### cut from the original position
        self.length -= 1

    def addToHead(self, node): ### if a node is added to a list, it must be the most recently used, so add to head
        node.prev, node.next = self.head, self.head.next ### insert
        self.head.next.prev = node ### link
        self.head.next = node ### link
        self.length += 1

    def deleteTail(self):
        if self.length > 0:
            node = self.tail.prev
            self.tail.prev = node.prev
            node.prev.next = self.tail
            node.prev, node.next = None, None ### C/C++ style
            self.length -= 1
            return node


class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.minFreq = 1
        self.hashTable = {} ### {key: node}
        self.cache = {} ### {freq: LRU Cache(DLinkedList)}
        
    def get(self, key):
        if key not in self.hashTable:
            return -1
        else:
            node = self.hashTable[key]
            
            ### delete from old freq list
            freqList = self.cache[node.freq]
            freqList.delete(node)
            if freqList.length == 0:
                del self.cache[node.freq]
                if node.freq == self.minFreq:
                    self.minFreq += 1

            ### add to new freq list
            node.freq += 1
            if node.freq not in self.cache:
                self.cache[node.freq] = DLinkedList(node.freq)
            self.cache[node.freq].addToHead(node)

            return node.val

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.hashTable:
            node = self.hashTable[key]
            node.val = value
            
            ### delete from old freq list
            freqList = self.cache[node.freq]
            freqList.delete(node)
            if freqList.length == 0:
                del self.cache[node.freq]
                if node.freq == self.minFreq:
                    self.minFreq += 1

            ### add to new freq list
            node.freq += 1
            if node.freq not in self.cache:
                self.cache[node.freq] = DLinkedList(node.freq)
            self.cache[node.freq].addToHead(node)

            return
          
        if self.size == self.capacity:
            freqList = self.cache[self.minFreq]
            nodeToDel = freqList.deleteTail()
            del self.hashTable[nodeToDel.key]
            if freqList.length == 0:
                del self.cache[self.minFreq]
        else:
            self.size += 1

        ### Add the new node
        node = DLinkedNode(key, value)
        self.minFreq = 1 
        if 1 not in self.cache:
            self.cache[1] = DLinkedList(1)
        self.cache[1].addToHead(node)
        self.hashTable[key] = node
 


### Hash Table + Balanced BST (Heap)
### TC: O(logC) SC: O(C) where C is the capacity of the cache
'''
灵异事件 册那 leetcode线下能过，线上魔幻bug
'''
import time
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.time = time.time()
        self.idx = -1

    def __gt__(self, node):
        if self.freq > node.freq:
            return True
        elif self.freq == node.freq:
            return self.time > node.time
        else:
            return False

class minHeap:
    heap = []

    def siftUp(self, idx):
        if idx > 0: ### still can sift up
            parent = (idx - 1) // 2
            if self.heap[parent] > self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent] ### swap
                self.heap[parent].idx = parent
                self.heap[idx].idx = idx
                self.siftUp(parent)

    def siftDown(self, idx):
        left  = 2*idx + 1
        right = 2*idx + 2
        if right < len(self.heap):
            if self.heap[left] > self.heap[idx] and self.heap[right] > self.heap[idx]:
                return
            if self.heap[left] > self.heap[right]: ### trick: swap with the smaller child 
                self.heap[right], self.heap[idx] = self.heap[idx], self.heap[right]
                self.heap[right].idx = right
                self.heap[idx].idx = idx
                self.siftDown(right)
            else:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left]
                self.heap[left].idx = left
                self.heap[idx].idx = idx
                self.siftDown(left)

        elif left < len(self.heap):
            if self.heap[idx] > self.heap[left]:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left]
                self.heap[left].idx = left
                self.heap[idx].idx = idx
                self.siftDown(left)


    def __len__(self):
        return len(self.heap)

    def push(self, node):
        self.heap.append(node)
        node.idx = len(self.heap) - 1
        self.siftUp(len(self.heap)-1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        else:
            top = self.heap[0]
            bottom = self.heap.pop() ### trick
            if self.heap:
                self.heap[0] = bottom
                self.siftDown(0)
            return top

    def top(self):
        if len(self.heap) == 0:
            return None
        else:
            return self.heap[0]



class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = minHeap()
        self.cache = {}
        

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            idx = node.idx
            node.freq += 1
            node.time = time.time()
            self.heap.siftDown(idx)
            return node.value
        else:
            return -1
        

    def put(self, key, value):
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            node.freq += 1
            node.time = time.time()
            self.heap.siftDown(node.idx)
        else:
            if len(self.heap) == self.capacity:
                nodeToDel = self.heap.pop()
                del self.cache[nodeToDel.key]
            nodeToAdd = Node(key, value)
            self.cache[key] = nodeToAdd
            self.heap.push(nodeToAdd)



test = LFUCache(3)

test.put(2,2)
test.put(1,1)
test.get(2)
test.get(1)
test.get(2)
test.put(3,3)
test.put(4,4)
test.get(3)
test.get(2)
test.get(1)
test.get(4)