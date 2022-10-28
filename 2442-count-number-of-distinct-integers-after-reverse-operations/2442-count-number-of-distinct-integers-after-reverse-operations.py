class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        
        def reverse(n):
            
            n = str(n)[::-1]
            i = 0
            
            while n[i] == "0":
                i += 1
            return int(n[i:])
        
    
        distinct = set()
        
        
        for i in range(len(nums)):
            distinct.add(nums[i])
            distinct.add(reverse(nums[i]))
            
        return len(distinct)