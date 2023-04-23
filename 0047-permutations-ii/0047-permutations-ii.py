class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = []
        perm = []
        
        count = Counter(nums)
        
        def dfs():
            
            if len(perm) == len(nums):
                ans.append(perm[:])
                return
            
            
            for item in count:
                if count[item] > 0:
                    
                    count[item] -= 1
                    perm.append(item)
                    
                    dfs()
                    
                    perm.pop()
                    count[item] += 1
                    
        dfs()
        
        
        return ans
                    
                    
            
                
                
                
        
        