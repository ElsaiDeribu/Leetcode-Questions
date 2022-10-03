class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        
        order= []
        ans = []
        
        
        for i in range(len(arr)):
            order.append((abs(x-arr[i]), arr[i]))
            
        order.sort()
        
        
        for i in range(k):
            ans.append(order[i][1])
            
        ans.sort()
        
        return ans
        
        