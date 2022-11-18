class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        primes = [2, 3, 5]
        heap = []
        visited = set()
        heappush(heap, 1)
        
        while n:
            curr = heappop(heap)
            for i in primes:
                if curr * i not in visited:
                    visited.add(curr * i)
                    heappush(heap, curr * i)
                    
            n -= 1
            
        return curr