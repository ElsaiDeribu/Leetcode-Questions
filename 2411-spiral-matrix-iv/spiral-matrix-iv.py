# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        ans = [[0] * n for _ in range(m)]

        direction = "right"
        top = left = 0
        right = n - 1
        bottom = m - 1

        while left <= right and bottom >= top:

            if direction == "right":
                for c in range(left, right + 1):
                    ans[top][c] = head.val if head else -1
                    head = head.next if head else None

                direction = "down"
                top += 1

            elif direction == "down":
                for r in range(top, bottom + 1):
                    ans[r][right] = head.val if head else  -1
                    head = head.next if head else None

                direction = "left"
                right -= 1

            elif direction == "left":
                for c in range(right, left - 1, -1):
                    ans[bottom][c] = head.val if head else -1
                    head = head.next if head else None

                direction = "up"
                bottom -= 1

            elif direction == "up":
                for r in range(bottom, top - 1, -1):
                    ans[r][left] = head.val if head else -1
                    head = head.next if head else None

                direction = "right"
                left += 1


        return ans

        