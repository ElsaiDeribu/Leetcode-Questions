class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        grades.sort()
        
        total = 0
        count = 0
        lastCount = 1
        lastTotal = grades[0]
        ans = 1
        
        for i in range(1, len(grades)):
            total += grades[i]
            count += 1
            
            if total > lastTotal and count > lastCount:
                lastTotal = total
                lastCount = count
                total = 0
                count = 0
                ans += 1
            
                
            
            
            
            
            
        return ans
        
        