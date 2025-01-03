# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)
        
    def helper(self, node):
        if not node:
            return 0
        
        return max(self.helper(node.left), self.helper(node.right)) + 1