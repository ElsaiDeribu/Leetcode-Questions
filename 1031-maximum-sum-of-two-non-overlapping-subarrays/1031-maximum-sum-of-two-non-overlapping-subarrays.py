class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        
        l = 0
        subArrSum = 0
        firstLenArr = []
        secondLenArr = []
        ans = 0
        
        for i in range(firstLen):
            
            subArrSum += nums[i]
            r = i
        
        firstLenArr.append((l, r, subArrSum))

        
        while r < len(nums):
            
            r += 1
            if r < len(nums):
                subArrSum += nums[r]
            
            subArrSum -= nums[l]
            l += 1
            
            if r < len(nums):
                firstLenArr.append((l, r, subArrSum))
                
        
        subArrSum = 0
        l = 0
        
        
        for i in range(secondLen):
            
            subArrSum += nums[i]
            r = i
        
        secondLenArr.append((l, r, subArrSum))

        
        while r < len(nums):
            
            r += 1
            if r < len(nums):
                subArrSum += nums[r]
            
            subArrSum -= nums[l]
            l += 1
            
            if r < len(nums):
                secondLenArr.append((l, r, subArrSum))
                
        
        for i in range(len(firstLenArr)):
            for j in range(len(secondLenArr)):
                
                if (firstLenArr[i][1] < secondLenArr[j][0]) or (firstLenArr[i][0] > secondLenArr[j][1]):
                    
                    ans = max(ans, firstLenArr[i][2] + secondLenArr[j][2])
                    
                
                
        return ans
        
        
        
            
            
            
            
            
        