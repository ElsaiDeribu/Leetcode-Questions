class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        sortedArr = [(index, value) for index, value in enumerate(arr)]
        
        sortedArr = sorted(sortedArr, key = lambda x: x[1])
        
        j = len(arr) - 1
        
        for i in range(len(arr) - 1):
            
            while sortedArr[j][0] <= i:
                j -= 1
            
            arr[i] = sortedArr[j][1]
            
        arr[-1] = -1   
        return arr