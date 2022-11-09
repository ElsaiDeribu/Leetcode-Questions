class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        size = 0
        for i in range(len(trips)):
            size = max(size, trips[i][2])
        
        prefixes = [0] * (size + 1)
        
        for i in range(len(trips)):
            prefixes[trips[i][1]] += trips[i][0]
            prefixes[trips[i][2]] -= trips[i][0]
        
        print(prefixes)
        for i in range(1, len(prefixes)):
            prefixes[i] = prefixes[i - 1] + prefixes[i]
            
        for i in range(len(prefixes) - 1):    
            if i < len(prefixes) and prefixes[i] > capacity:
                return False
            
        return True
                
            
        