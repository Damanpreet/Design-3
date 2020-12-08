# Space complexity - O(2c) for reference dictionary and linked list nodes.
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        # sentinels
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1) 
        # initialize a doubly linked list.
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.refDict = dict()
        
    def __delete_node(self, refNode):
        '''
        Function to remove the previous node reference.
        '''
        refNode.next.prev = refNode.prev
        refNode.prev.next = refNode.next
    
    def __add_node_to_head(self, refNode):
        '''
        Function to move the least recently added node to the head.
        '''
        refNode.next = self.head.next
        self.head.next.prev = refNode
        self.head.next = refNode
        refNode.prev = self.head
        
    def __delete_node_from_tail(self):
        '''
        Function to delete the node from the tail if the maximum capacity of lru cache is reached.
        '''
        delNode = self.tail.prev
        self.__delete_node(delNode)
        return delNode.key
        

    ## Time complexity - O(1)
    def get(self, key: int) -> int:
        # Since we need reference to the previous node to assign the value, we will use doubly linked list.
        # if the key does not exist, cannot get the value
        if self.capacity == 0 or key not in self.refDict:
            return -1
        
        # get the pointer to the reference node from the hash map.
        refNode = self.refDict[key]
        
        # adjust the node location
        # 1 (Time - O(1) we have the reference to the pointers)
        # 2 - no need to update the value (Time - O(1) directly add node to the head)
        self.__delete_node(refNode)         
        self.__add_node_to_head(refNode)    
        
        return refNode.value
        
        
    ## Time complexity - O(1)
    def put(self, key: int, value: int) -> None:
        # edge case
        if self.capacity == 0:
            return 
        
        # CASE 1 - check whether the node exists
        if key in self.refDict:
            # 1- get the pointer to the reference node from the hash map.
            # 2- update the node value.
            refNode = self.refDict[key]
            self.__delete_node(refNode)              
            refNode.value = value                    
        else:   # CASE 2        
            # 1 - delete node from the tail (FIFO)
            # remove from the hashMap
            if len(self.refDict) == self.capacity:
                delNode = self.__delete_node_from_tail() 
                del self.refDict[delNode]    
                
            # create a reference node
            refNode = Node(key, value)                   
            self.refDict[key] = refNode
        
        # 2 - no need to update the value  
        self.__add_node_to_head(refNode)     
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Using orderred dictionary in python
# Space complexity - O(C) where C is the capacity of the lru cache
import collections
class LRUCache:
    def __init__(self, capacity: int):
        # ordered dictionary in python uses a doubly linked list and hashmap (similar to approach 1)
        self.orderedDict = collections.OrderedDict()
        self.cap = capacity
        
    # Time complexity - O(1)
    def get(self, key: int) -> int:
        if key not in self.orderedDict:
            return -1
        # pop from the ordereddictionary and add it back.
        value = self.orderedDict.pop(key)
        self.orderedDict[key] = value
        return value
        
    # Time complexity - O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.orderedDict:
            self.orderedDict.pop(key)
        elif len(self.orderedDict) == self.cap:
            self.orderedDict.popitem(last=False)
        # add to the ordered dictionary
        self.orderedDict[key] = value
        