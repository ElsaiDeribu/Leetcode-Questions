class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        windowElements = defaultdict(int)
        maxCount = 0
        left = 0
        
        
        for right in range(len(fruits)):
            
            windowElements[fruits[right]] += 1
            
            while len(windowElements) > 2:
                 
                windowElements[fruits[left]] -= 1

                if windowElements[fruits[left]] == 0:
                    del windowElements[fruits[left]]
                    
                left += 1
                
            if len(windowElements) <= 2:
                
                currSum = 0
                for val in windowElements.values():
                    currSum += val
                
                maxCount = max(maxCount, currSum)
                
        return maxCount
                
       