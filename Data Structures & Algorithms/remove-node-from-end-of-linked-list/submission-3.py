class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Reverse the linked list
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        new_head = prev
        
        # Step 2: Handle edge case where we remove the first node of the reversed list 
        # (which corresponds to the last node of the original list)
        if n == 1:
            new_head = new_head.next
        else:
            # Traverse to the node just before the target
            curr = new_head
            for _ in range(n - 2):
                curr = curr.next
            curr.next = curr.next.next
            
        # Step 3: Reverse the list back to original order
        prev = None
        curr = new_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev