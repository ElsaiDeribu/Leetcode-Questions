class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = [[]]
        curr = []
        
        def recur(start = 0):
            if start >= len(nums):
                return
            
            for i in range(start, len(nums)):
                
                curr.append(nums[i])
                ans.append(curr[:])
                recur(i + 1)
                
                curr.pop()
                
        recur() 
        
        return ans
        
        
        