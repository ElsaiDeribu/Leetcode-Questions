class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        comb = []
        ans = []
        
        def dfs(index):
            if index == len(nums):
                return
            
            for i in range(index, len(nums)):
                    
                if nums[i] >= comb[-1]:
                    comb.append(nums[i])
                    ans.append(comb[:])
                    
                dfs(i + 1)
                if nums[i] >= comb[-1]:
                    comb.pop()
        
        
        for i in range(len(nums)):
            comb.append(nums[i])
            dfs(i + 1)
            comb.pop()
        
        ans = sorted(list(map(list, set(map(tuple, ans)))))
        
        return ans