class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        
        def getCount(num):
            
            count = 0
            num = str(bin(num))
            
            for b in num:
                if b == "1":
                    count += 1
                    
            return count
        
        
        for i in range(len(arr)):
            arr[i] = (getCount(arr[i]), arr[i])
            
        arr.sort()
        
        
        return [tup[1] for tup in arr]
        