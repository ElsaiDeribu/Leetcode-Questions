class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        left, right = 0, len(nums) - 1
        p1, p2  = 0, 0
        turn = 1
        
        @cache
        def helper(left, right, turn):
            
            if left > right:
                return 0
            
            
            if turn == 1:
                
                poss1 = nums[left] + helper(left + 1 , right, 2)
                poss2 = nums[right] + helper(left, right - 1, 2)

                return max(poss1, poss2)
            
            else:
                
                poss1 = -nums[left] + helper(left + 1 , right, 1)
                poss2 = -nums[right] + helper(left, right - 1, 1)

                return min(poss1, poss2)
                
        return helper(left, right, turn) >= 0