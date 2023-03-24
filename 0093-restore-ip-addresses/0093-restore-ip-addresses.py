class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        ans = []
        comb = []
       
        def dfs(index):
            
            if len(comb) == 4:
                if index == len(s):
                    ans.append(".".join(comb)) 
                return
        
            for i in range(index, index + 3):
                val = s[index: i + 1]
                comb.append(val)
                
                if len(val) > 1:
                    if val[0] != "0" and int(val) <= 255:
                        dfs(i + 1) 
                else:    
                    dfs(i + 1)
                    
                comb.pop()
        
        
        for i in range(3):
            val = s[:i + 1]
            comb.append(val)
            
            if len(val) > 1:
                if val[0] != "0" and int(val) <= 255:
                    dfs(i + 1) 

            else:    
                dfs(i + 1)
            
            comb.pop()
            
        return ans
            