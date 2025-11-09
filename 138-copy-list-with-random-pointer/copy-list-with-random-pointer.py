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
        

        dummy = curr = Node(0)
        main_curr = head
        dic = {}

        while main_curr:

            curr.next = Node(main_curr.val)
            dic[main_curr] = curr.next
            
            curr = curr.next
            main_curr = main_curr.next

        curr = dummy.next
        main_curr = head

        while main_curr:

            if main_curr.random:
                curr.random = dic[main_curr.random]

            curr = curr.next
            main_curr = main_curr.next



        return dummy.next


