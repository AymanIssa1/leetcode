# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        count = [k]
        result = [None]
        self.helper(root, count, result)
        return result[0]


    def helper(self, node, count, result):
        if not node:
            return

        if node.left:
            self.helper(node.left, count, result)

        count[0] -= 1
        if count[0] == 0:
            result[0] = node.val
            return

        if node.right:
            self.helper(node.right, count, result)