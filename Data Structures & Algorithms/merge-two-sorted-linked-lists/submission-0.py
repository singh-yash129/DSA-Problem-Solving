# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting point
        dummy = ListNode()
        # 'current' acts as our pointer to build the new list
        current = dummy
        
        # Traverse both lists as long as neither is empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            # Move our current pointer forward
            current = current.next
            
        # If one of the lists is exhausted, attach the remaining part of the other list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        # The merged list starts at dummy.next
        return dummy.next