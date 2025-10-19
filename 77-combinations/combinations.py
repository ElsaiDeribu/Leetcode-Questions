class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        

        ans = []

        def dfs(lst, idx):
            if len(lst) == k:
                ans.append(lst[:])
                return

            for i in range(idx, n + 1):
                lst.append(i)
                dfs(lst, i + 1)
                lst.pop()

        dfs([], 1)

        return ans



            