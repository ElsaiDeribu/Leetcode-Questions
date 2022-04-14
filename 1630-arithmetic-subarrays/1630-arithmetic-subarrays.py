class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        arth = 0
        for i in range(len(l)):
            subArr = nums[l[i]:(r[i] + 1)]
            subArr.sort()
            d =  subArr[1] - subArr[0] 
            for j in range(len(subArr)-1):
                if( (subArr[j+1] - subArr[j] ) != d):
                    arth = 0
                    break
                else:
                    arth = 1

            if arth :
                ans.append (True)
            else: 
                ans.append(False)
        return ans
                    
                    