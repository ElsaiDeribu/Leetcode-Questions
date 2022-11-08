class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        count = 0
        
        for i in range(len(arr1)):
            count += 1
            for j in range(len(arr2)):
                if abs(arr2[j] - arr1[i]) <= d:
                    count -= 1
                    break
                    
        # for i in arr1:
        #     if i != '':
        #         count += 1
                
        return count
            
