class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        nums.sort()
        
        mid = nums[math.floor(len(nums)/2)]
        moves = 0
        
        
        for i in range(len(nums)):
            
            if nums[i] > mid:
                moves += (nums[i] - mid)
                
            if nums[i] < mid:
                moves += (mid - nums[i])
                
                
        return moves
            
            
