class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
            
        len_val = 0
        prior = ListNode()
        pre = prior
        curr = head
        dummy = ListNode()
        target = dummy
        
        while curr:
            len_val += 1
            
            if left <= len_val and len_val <= right:
                # Collect the nodes to be reversed
                target.next = ListNode(curr.val)
                target = target.next
            elif len_val < left:
                pre.next = ListNode(curr.val)
                pre = pre.next
            else:
                break
            curr = curr.next
            
        tru = dummy.next
        prev = None

        # Reverse the target sub-list
        while tru:
            nxt = tru.next
            tru.next = prev
            prev = tru
            tru = nxt
  
        pre.next = prev
        
        # Find the tail of the reversed sub-list to attach the remaining part (`curr`)
        tail = pre.next
        while tail and tail.next:
            tail = tail.next
            
        if tail:
            tail.next = curr

        return prior.next