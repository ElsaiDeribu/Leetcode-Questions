class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        
        temp = sorted([(scores[i], ages[i]) for i in range(len(ages))])
        dp = [temp[i][0] for i in range(len(ages))]
        
        for i in range(len(ages)):
            for j in range(i):
                if temp[j][1] <= temp[i][1]:
                    dp[i] = max(dp[i], dp[j] + temp[i][0])
                    
        
        return max(dp)
        
      
    
    
        # temp = [(ages[i], scores[i]) for i in range(len(ages))]
        # temp.sort()
        
#         @cache
#         def dp(maxScore, age,  idx):
            
#             if idx >= len(ages):
#                 return 0
            
#             if temp[idx][1] < maxScore and temp[idx][0] > age:
                
#                 res = dp(maxScore,age, idx + 1)
#                 return res
                
#             else:
#                 res = dp(maxScore,age, idx + 1)
#                 if temp[idx][1] > maxScore:
#                     age = temp[idx][0]
                    
#                 res2 = dp(max(maxScore,temp[idx][1]), age, idx + 1) + temp[idx][1] 
                
                
#                 return max(res, res2)
            
            
#         return dp(float("-inf"), float("inf") ,0)
                
            
                
            
            