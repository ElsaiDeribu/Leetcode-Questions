class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        ans = [0]*len(nums)
        ans[0] = nums[0]
        dek = deque()
        dek.append((nums[0],0))
        
        for i in range(1,len(nums)):
            
            while dek[0][1] < i - k:
                dek.popleft()
 
            toinsert = dek[0][0] + nums[i]   
            while dek and dek[-1][0] < toinsert:
                dek.pop()
            dek.append((toinsert,i))

            ans[i] = dek[-1][0] 
            
    
        
        return ans[-1]