# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        output = []

        curr_queue = [root]
        next_queue = []

        while curr_queue:
            if len(curr_queue) == 1:
                output.append(curr_queue[0].val)
            
            curr_node = curr_queue.pop(0)

            if curr_node.left:
                next_queue.append(curr_node.left)
                
            if curr_node.right:
                next_queue.append(curr_node.right)
            
            if len(curr_queue) == 0:
                curr_queue, next_queue = next_queue, []

        return output