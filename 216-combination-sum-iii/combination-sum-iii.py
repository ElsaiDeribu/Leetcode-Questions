class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []

        def recur(start, arr, k, n):

            if k == 0 and n == 0:
                ans.append(arr[:])
                return

            if n < 0 or k < 0:
                return

            for num in range(start, 10):

                recur(num + 1, arr + [num], k - 1, n - num )


        recur(1, [], k, n)

        return ans



        