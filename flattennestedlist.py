# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """

#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """

#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# Requires extra space (Not a good solution)
# Time complexity - O(1)  # for next and hasNext
# Space complexity - O(n) # n is the length of all integers in a nested list.
# Did this solution run on leetcode? - yes
from collections import deque
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # flatten the nested list and maintain it in a queue.
        self.flattenList = deque()
        self.__flatten(nestedList)
      
    def __flatten(self, nestedList):
        for element in nestedList:
            if element.isInteger():
                self.flattenList.append(element.getInteger())
            else:
                self.__flatten(element.getList())
    
    def next(self) -> int:
        if len(self.flattenList) == 0:
            return 
        return self.flattenList.popleft()
    
    def hasNext(self) -> bool:
        return len(self.flattenList) > 0
        

# Avg. Time complexity - O(1) worst case - O(n) if list within a list, asymptotically O(1)
# Avg. Space complexity - O(1) 
# Did this solution run on leetcode? - yes
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nextelem = None
        self.stack = [iter(nestedList)] # iterator on the nested integer
        
    def next(self) -> int:
        # we can implement another iterator and 
        return self.nextelem.getInteger()
    
    def hasNext(self) -> bool:
        '''
        1. since the user checks hasnext first and then moves to the next. 
        2. we can implement our logic to fetch the next element in the hashnext and use this value in the next function.
        '''
        while self.stack:
            self.nextelem = next(self.stack[-1], None)
            # case 1 - iterator has reached the end.
            if self.nextelem is None:
                self.stack.pop()
            # case 2 - if the next element is an integer.
            elif self.nextelem.isInteger():
                return True
            # case 3 - if the next element is a list.
            else:
                self.stack.append(iter(self.nextelem.getList()))
            
        return False
            
            

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())