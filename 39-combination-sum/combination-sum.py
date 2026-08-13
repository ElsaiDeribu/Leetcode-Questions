class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: 
                
        # n = number of candidates
        # T = target
        # m = minimum candidate value
        # L = floor(T / m) = maximum combination length
        # C = number of valid combinations
        #
        # TC: O(C(n + L, L) + L·C)
        # SC: O(n + L) auxiliary, O(n + L + L·C) including output

        ans = []
        perm = []

        def dfs(idx, left_over):

            if left_over == 0:
                ans.append(perm[:])
                return

            if left_over < 0 or idx == len(candidates):
                return 

            perm.append(candidates[idx])
            dfs(idx, left_over - candidates[idx])
            perm.pop()

            dfs(idx + 1, left_over)


        dfs(0, target)

        return ans
      
        
        
        # ans = []
        # perm = []

        # def dfs(idx, left_over):

        #     if left_over < 0 or idx == len(candidates):
        #         return 

        #     if left_over == 0:
        #         ans.append(perm[:])
        #         return


        #     perm.append(candidates[idx])
        #     dfs(idx, left_over - candidates[idx])
        #     perm.pop()


        #     dfs(idx + 1, left_over)


        # dfs(0, target)

        # return ans




        