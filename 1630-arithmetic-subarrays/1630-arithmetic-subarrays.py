class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        ans = []
        def isArithmetic(arr):
            d = arr[1] - arr[0]
            for i in range(len(arr) - 1):
                if arr[i + 1] - arr[i] != d:
                    return False
            return True
        
        for i in range(len(l)):
            subarr = sorted(nums[l[i]: r[i] + 1])
            ans.append(isArithmetic(subarr))
            
        return ans
