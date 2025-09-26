class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def dfs(i, total, path):
            if total == target:
                ans.append(path[:])
                return
            if total > target or i == len(candidates):
                return

            # Choose the current candidate
            dfs(i, total + candidates[i], path + [candidates[i]])
            # Skip to the next candidate
            dfs(i + 1, total, path)

        dfs(0, 0, [])
        return ans


