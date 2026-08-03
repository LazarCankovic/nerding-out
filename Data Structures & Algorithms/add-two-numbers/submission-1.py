# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        first_dig = 0

        while l1 or l2 or first_dig:
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + first_dig

            second_dig = total % 10
            first_dig = total // 10

            cur.next = ListNode(second_dig)

            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return res.next