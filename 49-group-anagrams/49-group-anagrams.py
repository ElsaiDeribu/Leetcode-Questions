class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        
        ans = []
        buckets = defaultdict(list)
        
        for i in strs:
            
            buckets[''.join(sorted(i))].append(i)
            
        for i in buckets.values():
            ans.append(i)
            
        return ans
            
            
            
            
            
         # ans = []
  
        
#         for i in strs:
#             found = 0
#             if len(buckets) == 0:
#                 ans.append([i])
#             else:
#                 for j in range(len(ans)):
#                     if Counter(ans[j][0]) == Counter(i):
#                         ans[j].append(i)
#                         found = 1
#                         break
#                 if not found:        
#                     ans.append([i])
                
#         return ans
                
        
            
        