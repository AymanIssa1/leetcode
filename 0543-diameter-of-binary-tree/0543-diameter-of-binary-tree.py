# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.diameter = 0
        
        self.diameterOfBinaryTreeHelper(root)

        return self.diameter


    def diameterOfBinaryTreeHelper(self, root):
        if not root:
            return 0
        
        left_sum = self.diameterOfBinaryTreeHelper(root.left)
        right_sum = self.diameterOfBinaryTreeHelper(root.right)

        self.diameter = max(self.diameter, left_sum + right_sum)

        return max(left_sum, right_sum) + 1
        