# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""

        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next

        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        
        num1 = int(num1)
        num2 = int(num2)

        result = num1 + num2

        curr_node = None
        for val in str(result):
            new_node = ListNode(val)
            new_node.next = curr_node
            curr_node = new_node

        return curr_node