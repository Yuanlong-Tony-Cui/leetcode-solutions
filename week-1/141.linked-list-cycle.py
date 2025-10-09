# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # NOTE:
        # - Use fast & slow pointers to detect loops

        # if not head:
        #     return False
        # Base case already covered by the while loop

        slow = fast = head
        while slow and slow.next and fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
