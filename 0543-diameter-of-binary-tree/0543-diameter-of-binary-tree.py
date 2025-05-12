# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.helper(root)
        return self.diameter
    
    def helper(self, node):
        if not node:
            return 0
        
        left_sum = self.helper(node.left)
        right_sum = self.helper(node.right)

        self.diameter = max(self.diameter, left_sum + right_sum)

        return max(left_sum, right_sum) + 1



        