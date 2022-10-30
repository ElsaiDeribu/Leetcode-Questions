class Solution:
    def trimMean(self, arr: List[int]) -> float:
        
        arr.sort()
        
        nOfItms= int(len(arr) * 0.05)
        
        length = len(arr) - (2 * nOfItms)
        total = sum(arr[nOfItms:len(arr) - nOfItms])
        
        return total/ length