# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create 2 pointers for iterating through the list so to reverse
        prev, curr = None, head
        
        # while the curr pointer isnt null
        while curr:
        # temp next ptr will point to the next node of curr
            next = curr.next
        # the next node of current is now the previous ptr
            curr.next = prev
        # previous pointer is now the current node
            prev = curr
        # the current pointer is now on the temp (next) node
            curr = next
        return prev