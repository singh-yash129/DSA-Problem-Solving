class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize dummy node pointing to the head
        dummy = ListNode(0, head)
        length = 0
        curr = head
        
        # Calculate length of the list
        while curr:
            length += 1
            curr = curr.next
            
        # Traverse to the node before the one to be removed
        curr = dummy
        for _ in range(length - n):
            curr = curr.next
            
        # Remove the Nth node
        curr.next = curr.next.next
        
        return dummy.next