class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        for i in range(len(piles)):
            piles[i] = -piles[i]
            
        heapify(piles)  
            
        while k:
            largest = -heappop(piles)
            largest = largest - (largest // 2)
            heappush(piles, -largest)
            k -= 1
          
        return -sum(piles)