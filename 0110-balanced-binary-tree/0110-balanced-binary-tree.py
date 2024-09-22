# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        return self.helper(root) != -1
    
    def helper(self, node):
        if not node:
            return 0

        leftDepth = self.helper(node.left)
        rightDepth = self.helper(node.right)

        if leftDepth == -1 or rightDepth == -1 or abs(leftDepth - rightDepth) > 1:
            return -1

        return 1 + max(leftDepth, rightDepth)
