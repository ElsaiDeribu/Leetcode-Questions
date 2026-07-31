class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = set()
        perm = []

        def dfs(left_over):
            if left_over < 0:
                return 

            if left_over == 0:
                ans.add(tuple(sorted(perm[:])))
                return

            for _, val  in enumerate(candidates):
                perm.append(val)
                dfs(left_over - val)
                perm.pop()

        dfs(target)

        return list(ans)




        