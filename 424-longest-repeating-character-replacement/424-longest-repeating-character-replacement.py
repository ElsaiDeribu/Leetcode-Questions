class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 1
        
        chars = ['A','B','C','D','E','F','G','H','I','J','K',
                 'L','M','N','O','P','Q','R','S','T','U', 'V', 'W','X','Y','Z']
        
    
    
        for i in chars:
            print(i)

            l = 0 
            r = 0
            intruder = 0
            t = k


            while l < len(s):


                while r < len(s) and (s[r] == i or intruder < t ):

                    if s[r] != i:
                        intruder += 1
                    r += 1

                longest = max(longest, r - l)

                if s[l] != i:
                    intruder -= 1
                l += 1

        return longest
        
        
        
        
        
        
#         for i in range(len(s)):
#             j = i 
            
#             for e in chars:
#                 while j < len(s) and (e == s[j] or t)  :
#                     if e != s[j]:
#                         t -= 1
#                     if j != len(s):
#                         j += 1 

#                 longest = max(longest, j - i )
#                 # print(i,j)

#                 t = k
#                 j = i
            
#         return longest
            
        