class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ''
        str2 = ''

        curr = l1
        vurr = l2

        # 1. Extract digits into strings
        while curr:
            str1 += str(curr.val)
            curr = curr.next
        while vurr:
            str2 += str(vurr.val)
            vurr = vurr.next
        
        # 2. Reverse strings to form the actual numbers and add them
        # Since the list stores digits in reverse order, reversing the string back gives the correct integer
        val1 = int(str1[::-1])
        val2 = int(str2[::-1])

        curr_sum = val1 + val2
        dummy = ListNode()
        target = dummy

        # 3. Handle the sum of 0 explicitly, since the while loop skips when curr_sum == 0
        if curr_sum == 0:
            return ListNode(0)

        # 4. Rebuild the linked list from the sum
        while curr_sum != 0:
            rem = curr_sum % 10
            target.next = ListNode(rem)
            curr_sum = curr_sum // 10
            target = target.next

        return dummy.next