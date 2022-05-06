class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        boats = 0
        j = len(people) -1
        people.sort()
        while i <= j:
            if people[i] + people[j] <= limit:
                j -= 1
                i += 1
                boats += 1
            else:
                j -=  1
                boats += 1
        return boats
        
        