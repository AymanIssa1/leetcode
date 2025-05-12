# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        curr = head

        while curr:
            while len(stack) > 0 and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next

        head = None
        while stack:
            node = stack.pop()
            node.next = head
            head = node
        
        return head