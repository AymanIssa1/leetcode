# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        max_depth = self.getMaxDepth(nestedList, 1)
        
        result = [0]
        self.helper(nestedList, max_depth, result)
        return result[0]
        
    def helper(self, nestedList, depth, result):
        for ele in nestedList:
            if ele.isInteger():
                result[0] += (ele.getInteger() * depth)
            else:
                self.helper(ele.getList(), depth - 1, result)

    def getMaxDepth(self, nestedList, depth):
        max_depth = depth
        for ele in nestedList:
            if not ele.isInteger() and len(ele.getList()) > 0:
                max_depth = max(max_depth, self.getMaxDepth(ele.getList(), depth + 1))
        return max_depth