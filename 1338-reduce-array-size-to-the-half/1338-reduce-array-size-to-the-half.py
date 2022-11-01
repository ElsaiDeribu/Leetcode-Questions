class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        
        length = len(arr) 
        
        ans = 0
        countToRemove = 0
        arr = Counter(arr)
        
        arr = sorted(arr.items(), key = lambda x: x[1])
        
        for i in range(len(arr) - 1, -1, -1):
            
            countToRemove += arr[i][1]
            ans += 1

            if length - countToRemove <= length / 2:
                return ans
            
            
        
        