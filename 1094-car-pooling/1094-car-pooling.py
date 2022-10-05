class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        length = 0
        
        for num, f, t in trips:
            
            length =  max(length, t)
            
        ans = [0] * (length + 1)
        
        for nums, s, e in trips:
            ans[s] += nums
            ans[e] -= nums
        print(ans)
        
        if ans[0] > capacity:
            return False
        
        for i in range(1, len(ans)):
            ans[i] = ans[i] + ans[i - 1]
            
            if i < len(ans) - 1 and ans[i] > capacity:
                return False
            
            
        return True 
            
            
            
            