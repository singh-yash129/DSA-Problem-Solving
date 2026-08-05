class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
            
        len_val = 0
        prior = ListNode(0, head)
        pre = prior
        curr = head
        dummy = ListNode()
        target = dummy
        
        while curr:
            len_val += 1
            
            if left <= len_val and len_val <= right:
                target.next = ListNode(curr.val)
                target = target.next
            elif len_val < left:
                pre = pre.next
            else:
                break
            curr = curr.next
            
        tru = dummy.next
        prev = None

        while tru:
            nxt = tru.next
            tru.next = prev
            prev = tru
            tru = nxt
            
        # Connect the reversed portion to the rest of the list stored in `curr`
        tail = prev
        while tail and tail.next:
            tail = tail.next
            
        if tail:
            tail.next = curr
            
        pre.next = prev

        return prior.next