class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: 
        
        ans = []
        perm = []

        def dfs(idx, left_over):

            if left_over < 0 or idx == len(candidates):
                return 

            if left_over == 0:
                ans.append(perm[:])
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




        