# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # creating an empty node list and the temp var for it
        res = ListNode()
        node = res

        while list1 and list2:
            # compare the values and add it to the merged one
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            # once the values are added, move the node to the next
            node = node.next
        # if one of the lists has more elements when the while loop ends, add the rest of the list
        if list1:
            node.next = list1
        else:
            node.next = list2
        # skipping the empty node
        return res.next


