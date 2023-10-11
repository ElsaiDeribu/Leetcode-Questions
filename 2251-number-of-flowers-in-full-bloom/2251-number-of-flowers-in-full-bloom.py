class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
        start =  sorted([ i for i, _ in flowers])
        end = sorted([i for _, i in flowers])
        ans = []
        
        for p in people:
            started = bisect_right(start, p)
            ended = bisect_left(end, p)
            ans.append(started-ended)
            
        return ans