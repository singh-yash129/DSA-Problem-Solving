# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        target = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                target.next = list1
                list1 = list1.next
            else:
                target.next = list2
                list2 = list2.next
            target = target.next
            
        if list1:
            target.next = list1
        elif list2:
            target.next = list2
            
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        res = None
        for lst in lists:
            res = self.mergeTwoLists(res, lst)
            
        return res