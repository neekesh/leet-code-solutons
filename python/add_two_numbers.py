# leet code problem number 1
# add two numbers:
# https://leetcode.com/problems/add-two-numbers/


from typing import Optional

class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            sum += carry
            if sum > 9:
                carry = 1
                current.next = ListNode(sum - 10)
            else: 
                current.next = ListNode(sum)

            
            current = current.next
        
        return dummy.next  