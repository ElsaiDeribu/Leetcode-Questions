class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans = []
        comb = []


        def dfs(idx, rem):

            if rem == 0:
                ans.append(comb.copy())
                return

            if rem < 0:
                return

            for i in range(idx, len(candidates)):

                if i > idx and candidates[i] == candidates[i - 1]:
                    continue

                comb.append(candidates[i])
                dfs(i + 1, rem - candidates[i])
                comb.pop()

        dfs(0, target)

        return ans



