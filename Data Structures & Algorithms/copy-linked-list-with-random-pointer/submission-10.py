import collections
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        my_dict = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            my_dict[cur] = copy
            cur = cur.next

        temp = head
        while temp:
            copy = my_dict[temp]
            copy.next = my_dict[temp.next]
            copy.random = my_dict[temp.random]  
            temp = temp.next
        return my_dict[head]
