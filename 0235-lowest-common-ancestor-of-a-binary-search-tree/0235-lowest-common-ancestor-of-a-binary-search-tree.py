# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, p, q)
        return self.lca
    
    def helper(self, curr_node, p, q):
        if not curr_node:
            return False

        left, right, mid = False, False, False

        if p == curr_node or q == curr_node:
            mid = True

        left = self.helper(curr_node.left, p, q)

        if not self.lca:
            right = self.helper(curr_node.right, p, q)

        if mid + left + right >= 2:
            self.lca = curr_node

        return mid or left or right
        