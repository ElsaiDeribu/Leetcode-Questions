class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        pile = []

        def dfs(idx):

            if idx == len(nums):
                ans.append(pile.copy())
                return
            
            #take
            pile.append(nums[idx])
            dfs(idx + 1)
            pile.pop()
 
            #not take
            dfs(idx + 1)


        dfs(0)

        return ans



        