# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # NOTE:
        # - In each iteration of the loop, alter the `next` attribute of the _current node_ only. Do not make any changes to the next node while in the current iteration!

        # if not head:
        #     return None
        # This base case is covered by the while loop

        curr = head
        prev = None
        while curr:
            next_node = curr.next  # store
            # Make each node point to its prev
            curr.next = prev
            prev = curr  # update
            curr = next_node  # update
        # At this point, `curr` is always None and `prev` always points to the last visited node
        return prev
