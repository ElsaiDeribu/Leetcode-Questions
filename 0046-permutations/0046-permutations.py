class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
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
                    
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def recur(arr):
            
#             if len(arr) == 1:
#                 return [arr.copy()] 
            
#             result = []
            
#             for _ in range(len(arr)):
#                 temp = arr.pop(0)
#                 perms = recur(arr)
#                 arr.append(temp)
                
#                 for perm in perms:
#                     perm.append(temp)
                
#                 result.extend(perms)
               
#             return result
        
        
        
#         return recur(nums)