# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        output = []
        level_result = []
        curr_queue = [root]
        next_queue = []

        while curr_queue:
            curr_node = curr_queue.pop(0)

            level_result.append(curr_node.val)

            if curr_node.left:
                next_queue.append(curr_node.left)

            if curr_node.right:
                next_queue.append(curr_node.right)

            if not curr_queue:
                output.append(level_result)
                level_result = []
                curr_queue, next_queue = next_queue, []

        return output