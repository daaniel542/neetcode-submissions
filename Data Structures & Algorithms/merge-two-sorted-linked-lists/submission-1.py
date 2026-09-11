# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

         # Create a dummy node to simplify building the merged list.
        # 'output' always points to the dummy node,
        # while 'node' points to the current end of the merged list.
        output = node = ListNode()

        # Continue while both lists still have nodes remaining.
        while list1 and list2:

            # Compare the current nodes of each list.
            # Attach the smaller node to the merged list,
            # then advance the pointer in that list.
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            # Move 'node' to the new end of the merged list.
            node = node.next

        # At least one list is now empty.
        # Attach the remaining nodes from the non-empty list.
        node.next = list1 or list2

        # Return the merged list, skipping the dummy node.
        return output.next



                


