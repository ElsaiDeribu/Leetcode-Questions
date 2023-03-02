class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        
        left, right = 0, len(nums) - 1
        p1, p2  = 0, 0
        turn = 1
        
        @cache
        def helper(p1, p2, left, right, turn):
            
            if left > right:
                return True if p1 >= p2 else False
            
            
            if turn == 1:
                
                poss1 = helper(p1 + nums[left], p2, left + 1 , right, 2)
                poss2 = helper(p1 + nums[right], p2, left, right - 1, 2)

                return poss1 or poss2
            
            else:
                
                poss1 = helper(p1, p2 + nums[left], left + 1 , right, 1)
                poss2 = helper(p1, p2 + nums[right], left, right - 1, 1)

                return poss1 and poss2
                
        return helper(p1, p2, left, right, turn)