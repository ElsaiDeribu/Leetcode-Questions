class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
        count = 0
        test = (minutesToTest / minutesToDie) + 1
        
        while test ** count < buckets:
            count += 1
            
            
        return count
        