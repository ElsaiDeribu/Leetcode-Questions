class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        ans = []
        last_index = defaultdict(int)
        
        for i in range(len(s)):
            last_index[s[i]] = max(last_index[s[i]], i )
           
        right = 0
        finishIndex = 0
        left = 0
        while right < len(s):
            finishIndex = max(finishIndex, last_index[s[right]])
            
            if finishIndex == right:
                ans.append(right - left + 1)
                finshIndex = 0
                left = right + 1
        
            right += 1
        
        return ans
        
        
        
#         ans = []
#         count = Counter(s)
#         window_elements = set()
#         l = 0
#         r = 0
#         while r < len(s):
#             window_elements.add(s[r])
#             while window_elements:
#                 if s[r] in window_elements:
#                     count[s[r]] -= 1
#                     if count[s[r]] == 0:
#                         window_elements.remove(s[r])
#                 else:
#                     window_elements.add(s[r])
#                     count[s[r]] -= 1
#                     if count[s[r]] == 0:
#                         window_elements.remove(s[r])
                    
#                 r += 1
                
#             ans.append(r - l)
#             l = r
            
#         return ans
                

                
                