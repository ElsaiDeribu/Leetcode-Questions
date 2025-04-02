class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

       
        def helper(num):
            if num == 1:
                return 0

            return (helper(num - 1) + k) % num


        return helper(n) + 1
             