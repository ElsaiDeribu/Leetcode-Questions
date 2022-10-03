class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        
        order = []
         
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                
                order.append((arr[i]/arr[j], [arr[i], arr[j]]))
                
        order.sort()
        
        return order[k - 1][1]
        