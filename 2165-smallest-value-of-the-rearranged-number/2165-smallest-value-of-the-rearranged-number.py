class Solution:
    def smallestNumber(self, num: int) -> int:
        
        negative = False
        
        if num < 0:
            negative = True
            
        num = str(num)
        
        lst = []
        
        
        if negative:
            for d in range(1,len(num)):
                lst.append(int(num[d]))
                
            for i in range(len(lst)):
                for j in range(i+1, len(lst)):
                    if lst[i] < lst[j]:
                        lst[j], lst[i] = lst[i], lst[j]        
            
            ans = ''.join(map(str, lst))
            return -int(ans)
             
                
        else:
            for d in range(0,len(num)):
                lst.append(int(num[d]))  
                
   
            for i in range(len(lst)):
                for j in range(i+1, len(lst)):
                    if i == 0 and lst[j] == 0:
                        continue

                    if lst[i] > lst[j]:
                        lst[j], lst[i] = lst[i], lst[j]

            ans = ''.join(map(str, lst))
            
            return int(ans)