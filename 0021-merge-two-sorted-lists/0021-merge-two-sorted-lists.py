# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node1 = list1
        node2 = list2

        dummy_node = ListNode(-1)
        curr = dummy_node

        while node1 and node2:
            if node1.val > node2.val:
                curr.next = node2
                node2 = node2.next
            else:
                curr.next = node1
                node1 = node1.next

            curr = curr.next

        while node1:
            curr.next = node1
            curr = curr.next
            node1 = node1.next

        while node2:
            curr.next = node2
            curr = curr.next
            node2 = node2.next
        
        return dummy_node.next