# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr_max = float("-inf")
        curr_level = 1
        max_level = 1
        curr_level_values = []

        curr_queue, next_queue = [root], []
        while curr_queue:
            node = curr_queue.pop(0)
            curr_level_values.append(node.val)

            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)

            if not curr_queue:
                curr_sum = sum(curr_level_values)
                if curr_sum > curr_max:
                    curr_max = curr_sum
                    max_level = curr_level
                
                curr_level_values = []
                curr_level += 1
                curr_queue, next_queue = next_queue, []


        return max_level