class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        
        lessThanLargest = pow(2, p) - 2
        largest = lessThanLargest + 1
        divider = pow(10,9) + 7
        
        ans = pow(lessThanLargest, largest // 2,  divider) * largest % divider
        
        return ans
        
        
        