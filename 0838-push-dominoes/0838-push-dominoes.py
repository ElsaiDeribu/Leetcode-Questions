class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        
        forces = [0] * len(dominoes)
        f = 0
        ans = ""
        
        for i in range(len(dominoes)):
            
            if dominoes[i] == "R":
                f = len(dominoes)
            elif dominoes[i] == "L":
                f = 0
            else:
                f = max(f - 1, 0)
                
            forces[i] += f
        
        f = 0
            
        for j in range(len(dominoes) - 1, -1 , -1):
            
            if dominoes[j] == "R":
                f = 0
            elif dominoes[j] == "L":
                f = len(dominoes)
            
            else: 
                f = max(f - 1, 0)
                
            forces[j] -= f
           
            
        for i in range(len(dominoes)):
            
            if forces[i] == 0:
                ans += "."
            elif forces[i] < 0:
                ans += "L"
            elif forces[i] > 0:
                ans += "R"
                
                
        return ans