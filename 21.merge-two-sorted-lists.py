# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # NOTE:
        # - The "compare & add" loop is needed only when list1 and list2 both exist.
        # - The final returned ListNode is dummy_head.next, not dummy_head!

        curr = dummy_head = ListNode()
        # compare & add
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next  # proceed
        # NOTE: At this point, at least one of the two linked lists is None
        
        # Append the entire remaining list
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy_head.next