class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        top = sorted(score, reverse = True)
        dic = defaultdict(str)
      
        
        for i in range(len(top)):
            if i == 0:
                dic[top[i]] = "Gold Medal" 
                    
            elif i == 1:
                dic[top[i]] = "Silver Medal"
      
            elif i == 2:
                dic[top[i]] = "Bronze Medal"
                
            else:
                dic[top[i]] = str(i + 1)
        
        
        for i in range(len(score)):
            score[i] = dic[score[i]]

            
        return score