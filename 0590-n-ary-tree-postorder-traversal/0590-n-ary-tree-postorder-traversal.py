"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []
        self.helper(root, output)
        return output

    def helper(self, node, output):
        if not node:
            return

        for curr_node in node.children:
            self.helper(curr_node, output)
        
        output.append(node.val)

        