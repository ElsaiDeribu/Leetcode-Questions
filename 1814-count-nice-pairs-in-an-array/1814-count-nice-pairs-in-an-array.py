class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        def rev(n):
            if n == 0:
                return n
            n = str(n)
            n = n[::-1]
            
            i = 0 
            while n[i] == '0':
                i += 1
                
            return int(n[i:])
        
        
        prev = defaultdict(int)
        good = 0
        
        for j in range(len(nums)):
            
            good += prev[nums[j] - rev(nums[j])]
            
            prev[nums[j] - rev(nums[j])] += 1
            
            
        mod = 10**9 + 7
        
        return good % mod
            
            
            