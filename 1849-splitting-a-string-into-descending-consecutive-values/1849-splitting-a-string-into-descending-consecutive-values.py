class Solution:
    def splitString(self, s: str) -> bool:
        
        s = str((int(s)))
        
        
        def check(idx, prev):
            
            if idx == len(s):
                return True
            
            for j in range(idx, len(s)):
                curr = int(s[idx : j + 1])
                
                if prev - curr == 1 and check(j + 1, curr):
                    return True
                
            return False
        
        
        
        
        
        for i in range(len(s) - 1):
            
            curr = int(s[: i + 1])
            
            if check(i + 1, curr): return True
            
            
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(s)
        
#         comb = []
#         self.ans = False
        
        
#         def check(indices):
            
#             start = indices[0] + 1
#             prev = int(s[0: indices[0] + 1])
            
#             for i in range(1, len(indices)):
#                 # print(start, indices[i], prev)
#                 # print(indices)
#                 curr = int(s[start : indices[i] + 1])
                
#                 if prev - curr != 1 :
#                     return False
                
#                 start = indices[i] + 1
#                 prev = curr
            
           
#             curr = int(s[start:]) 

#             if prev - curr != 1 :
#                 return False

#             self.ans = True
#             return True
                
                
                
#         def recur(start = 0):
            
#             if start >= len(s) or self.ans:
#                 return
            
#             for i in range(start, len(s) - 1):
#                 comb.append(i)
#                 result = check(comb)
                
#                 if not result:
#                     return
#                 recur(i + 1)
#                 comb.pop()
                
#         recur()
        
#         return self.ans