class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        st = []
        rnge = []
        ans = 0
        
        for i in range(len(arr)):
            rnge.append([0,(arr[i], i), 0])
            arr[i] = (arr[i], i)
         
        
        for i in range(len(arr)):
            
            while st and st[-1][0] > arr[i]:
                
                rnge[st[-1][1]][2] = i
                
                st.pop()
                
            st.append((arr[i], i))
            
        for i in st:
            rnge[i[1]][2] = len(arr) 
            
        st = []
        
        for i in range(len(arr) - 1, -1, -1):
            
            while st and st[-1][0] > arr[i]:
                
                rnge[st[-1][1]][0] = i
                
                st.pop()
                
            st.append((arr[i], i))
            
        for i in range(len(st)):
            
            rnge[st[i][1]][0] = -1

                
                
        print(rnge)
            
        for i in rnge:
        
            if i[1][1] == 0:
                
                ans += i[1][0] *(i[2])
                
            else:
              
                ans += i[1][0] * ((i[1][1] - i[0]) * ( i[2] - i[1][1] ))
            
            
        return ans % (10**9 + 7)
            
            
            
            
                
            
        
        
        
        