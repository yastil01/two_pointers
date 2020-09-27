class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = prev = ListNode(-1)
        sum = 0
        while l1 or l2 or sum:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            curr = ListNode(sum%10)
            sum = sum // 10
            prev.next = curr
            prev = curr
        
        return dummy.next
