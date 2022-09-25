class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        
#         dictionary = {'a':0, 'b': 0, 'c':0}
#         count = 0
#         l = 0
        
#         for r in range(len(s)):
            
#             dictionary[s[r]] += 1
            
#             while dictionary['a'] > 0 and dictionary['b'] > 0 and dictionary['c'] > 0:
                
#                 dictionary[s[l]] -= 1
#                 l += 1
                    
#             count += l
#             print(count)
            
#         return count
                
        
        dictionary = {'a':0, 'b': 0, 'c':0}
        l = 0
        r = 0
        count = 0
            
        while r < len(s):
            
            dictionary[s[r]] += 1

            while (dictionary['a'] > 0 and dictionary['b'] > 0 and dictionary['c'] > 0):
                dictionary[s[l]] -= 1
                l += 1
                    
            count += l
            r += 1


        return count
                    
                
                
            
        
#         l = 0
#         count = 0
        
#         while l < len(s) - 2:
#             r = l + 2
            
#             while r < len(s):
#                 if 'a' in s[l:r + 1] and 'b' in s[l:r + 1] and 'c' in s[l:r + 1]:
#                     count += 1
#                 r += 1
            
#             l += 1
            
#         return count




#         count = 0
#         for l in range(len(s)):
#             for r in range(L + 2, len(s)):
#                 if 'a' in s[l:r + 1] and 'b' in s[l:r + 1] and 'c' in s[l:r + 1]:
#                     count += 1
                            
#         print(count)
                
        
        
            