class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        count = Counter(words)
        print(count)
        
        heap = []
        ans = []
        
        for i in count:
            heappush(heap, (-count[i], i))
         
            
        
        while k :
            ans.append(heappop(heap)[1])
            k -= 1
        return ans