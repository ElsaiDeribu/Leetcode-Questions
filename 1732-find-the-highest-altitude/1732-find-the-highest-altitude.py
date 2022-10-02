class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        
        highest = 0
        
        for i in range(len(gain)):
            if i == 0:
                highest = max(highest, gain[i])
                continue
                
            gain[i] = gain[i] + gain[i - 1]
            
            highest = max(highest, gain[i])

        return highest
            