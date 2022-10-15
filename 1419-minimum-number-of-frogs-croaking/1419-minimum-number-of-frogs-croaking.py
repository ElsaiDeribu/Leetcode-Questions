class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
        dic = {'c':0, 'r':0,'o':0,'a':0,'k':0,}
        
        seq = ['c','r','o','a','k']
        cf = 0
        
        count = Counter(croakOfFrogs)
        
        stdrd = count['c']
        
        for i in count.keys():
            if count[i] != stdrd:
                return -1
            
        
        for i in range(len(croakOfFrogs)):
            
            dic[croakOfFrogs[i]] += 1

            for j in range(seq.index(croakOfFrogs[i])):

                if dic[seq[j]] < dic[croakOfFrogs[i]]:
                           return -1

            if croakOfFrogs[i] == 'k':
                for i in range(len(seq)):
                    dic[seq[i]] -= 1

            cf = max(cf, dic[croakOfFrogs[i]])
                               
                               
        return cf
                    
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         dict = {'c':0, 'r':0,'o':0,'a':0,'k':0,}
#         cf = 0
        
        
#         for i in range(len(croakOfFrogs)):
            
#             if croakOfFrogs[i] == 'c':
#                 for i in dict.keys():
#                     if i != 'c':
                        
#                         dict[i] += 1
#                         cf = max(cf,dict[i])
                
#             else:
#                 dict[croakOfFrogs[i]] -= 1
#                 if dict[croakOfFrogs[i]] < 0:
#                     return -1
                
#         return cf
        