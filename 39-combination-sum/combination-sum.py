class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]: 
                
        # n — number of candidates
        # T — target
        # m — minimum candidate value
        # L — ⌊T / m⌋, maximum recursion depth from "take" moves (each take reduces left_over by at least m)

        # Upper bound:
        # TC: O(2^(n+L))
        # SC: O(2^(n+L))
        
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




        