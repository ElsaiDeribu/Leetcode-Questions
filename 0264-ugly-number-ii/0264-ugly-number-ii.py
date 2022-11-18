class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        mul = [2,3,5]
        vstd = set()
        heap = []
        heappush(heap, 1)
        
        while n:
            curr = heappop(heap)
            for i in mul:
                if curr * i not in vstd:
                    vstd. add(curr * i)
                    heappush(heap, curr * i)
                    
            n -= 1
            
        return curr