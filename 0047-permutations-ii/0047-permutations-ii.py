class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        
        def recur(arr):
            
            if len(arr) == 1:
                return [arr[:]] 
             
            result = []
            for i in range(len(arr)):
                n = arr.pop(0)
                nxt = recur(arr)
                arr.append(n)
                
                for item in nxt:
                    item.append(n)
                    
                result.extend(nxt)
                
            return result
        
        
        ans = recur(nums)
        
        for i in range(len(ans)):
            ans[i] = tuple(ans[i])
            
        return set(ans)
            
                
                
                
        
        