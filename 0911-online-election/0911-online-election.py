class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        
        maxTillNow = (1, persons[0])
        self.preProcessed = []
        votes = defaultdict(int)
        
        for i in range(len(persons)):
            
            votes[persons[i]] += 1
            if votes[persons[i]] >= maxTillNow[0]:
                maxTillNow = (votes[persons[i]], persons[i])
        
            self.preProcessed.append((times[i], maxTillNow[1]))
        
        
    def q(self, t: int) -> int:
        
        left = 0
        right = len(self.preProcessed) 
        
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if self.preProcessed[mid][0] <= t:
                left = mid
                
            else:
                right = mid
                
        return self.preProcessed[left][1]
            
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)