class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        
        left = 0
        right = len(people) - 1
        boatCount = 0
        
        
        while left <= right:
            
            if people[left] + people[right] <= limit:
                boatCount += 1
                left += 1
                right -= 1
            
            else:
                boatCount += 1
                right -= 1
                
                
        return boatCount
        